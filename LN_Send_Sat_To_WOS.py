#!/usr/bin/env python3.9
from argparse import ArgumentParser, Namespace
from requests import Response, get, post
from typing import TypedDict

# === CONFIGURATION ===
# You have to add Admin API key from LNbits
LNBITS_API_KEY: str = "xxx"
LNBITS_API_URL: str = "xxx"


class LNURLPayResponse(TypedDict):
    allowNostr: bool
    callback: str
    commitAllowed: int
    maxSendable: int
    metadata: str
    minSendable: int
    nostrPubkey: str
    pr: str
    tag: str


class PayReqResponse(TypedDict):
    pr: str


def get_lnurl_invoice(lightning_address: str, amount_sats: int):
    """
    Get invoice from Wallet of Satoshi

    ---
    :param lightning_address:
    :type lightning_address: str
    :param amount_sats:
    :type amount_sats:
    :return:
    :rtype:
    """
    name, domain = lightning_address.split("@")
    lnurlp_url = f"https://{domain}/.well-known/lnurlp/{name}"
    r1: Response = get(lnurlp_url)
    if r1.status_code != 200:
        raise Exception(f"Could not resolve lightning address: {r1.text}")
    data: LNURLPayResponse = r1.json()
    print(data)
    callback = data["callback"]
    r2: Response = get(callback, params={"amount": amount_sats * 1000})
    if r2.status_code != 200:
        raise Exception(f"Could not get invoice: {r2.text}")
    pay_req: PayReqResponse = r2.json()
    return pay_req["pr"]


def pay_invoice(bolt11_invoice) -> None:
    """
    Pay with LNBits

    ---
    :param bolt11_invoice:
    :type bolt11_invoice:
    :return: nothing
    :rtype: None
    """
    headers = {"X-Api-Key": LNBITS_API_KEY, "Content-type": "application/json"}
    data = {"out": True, "bolt11": bolt11_invoice}
    response = post(LNBITS_API_URL, json=data, headers=headers)
    if response.status_code == 201:
        print("✅ Payment sent successfully!")
        print("Payment hash:", response.json().get("payment_hash"))
    else:
        print("❌ Failed to send payment.")
        print("Status code:", response.status_code)
        print("Response:", response.text)


def main() -> None:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("address", help="Lightning Address provided by Wallet of Satoshi", type=str)
    parser.add_argument("amount", help="Amount of SATs to be sent to given address", type=int)
    args: Namespace = parser.parse_args()
    try:
        address: str = args.address
        amount: int = args.amount
        print(
            f"⚡ Getting invoice for {amount} sats to {address}..."
        )
        invoice = get_lnurl_invoice(address, amount)
        print("⚡ Paying invoice...")
        pay_invoice(invoice)
    except Exception as e:
        print("🔥 Error:", e)


if __name__ == "__main__":
    main()
