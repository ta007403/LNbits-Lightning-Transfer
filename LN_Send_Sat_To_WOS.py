import requests

# === CONFIGURATION ===
# You have to add Admin API key from LNbits
LNBITS_API_KEY = "xxx" 
LNBITS_API_URL = "xxx"
WOS_LIGHTNING_ADDRESS = "lyricalweather78@walletofsatoshi.com"  # <- you can put LN address here
AMOUNT_SATS = 90  # <- adjust amount here (satoshi)

# === GET INVOICE FROM WALLET OF SATOSHI ===
def get_lnurl_invoice(lightning_address, amount_sats):
    name, domain = lightning_address.split("@")
    lnurlp_url = f"https://{domain}/.well-known/lnurlp/{name}"

    r1 = requests.get(lnurlp_url)
    if r1.status_code != 200:
        raise Exception(f"Could not resolve lightning address: {r1.text}")
    data = r1.json()
    callback = data["callback"]

    r2 = requests.get(callback, params={"amount": amount_sats * 1000})
    if r2.status_code != 200:
        raise Exception(f"Could not get invoice: {r2.text}")
    return r2.json()["pr"]

# === PAY WITH LNBITS ===
def pay_invoice(bolt11_invoice):
    headers = {
        "X-Api-Key": LNBITS_API_KEY,
        "Content-type": "application/json"
    }
    data = {
        "out": True,
        "bolt11": bolt11_invoice
    }
    url = f"{LNBITS_API_URL}/api/v1/payments"
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print("✅ Payment sent successfully!")
        print("Payment hash:", response.json().get("payment_hash"))
    else:
        print("❌ Failed to send payment.")
        print("Status code:", response.status_code)
        print("Response:", response.text)

# === RUN ===
if __name__ == "__main__":
    try:
        print(f"⚡ Getting invoice for {AMOUNT_SATS} sats to {WOS_LIGHTNING_ADDRESS}...")
        invoice = get_lnurl_invoice(WOS_LIGHTNING_ADDRESS, AMOUNT_SATS)
        print("⚡ Paying invoice...")
        pay_invoice(invoice)
    except Exception as e:
        print("🔥 Error:", e)

