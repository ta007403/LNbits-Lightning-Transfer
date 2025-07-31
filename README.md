# LNbits Transfer to Wallet of Satoshi

## Script for Lightning transfer to Lightning Address provided by Wallet of Satoshi

### Prerequisites

* [git](https://git-scm.com/) - --fast-version-control
* [python](https://www.python.org) 3.9 and above - High-level general-purpose programming language
* [uv](https://docs.astral.sh/uv) - Extremely fast Python package & project manager, written in Rust

The following guide walks through setting up your local working environment using `git`
as distributed version control system and `uv` as Python package and version manager.
If you do not have `git` installed, run the following command.

<details>
  <summary> Install using Homebrew (Darwin) </summary>
  
  ```bash
  brew install git
  ```
</details>

<details>
  <summary> Install via binary installer (Linux or Windows Subsystem for Linux [WSL]) </summary>
  
  * Debian-based package management
  ```bash
  sudo apt install git-all
  ```

  * Fedora-based package management
  ```bash
  sudo dnf install git-all
  ```
</details>

<details>
  <summary> Install using Winget (Windows Powershell) </summary>
  
  ```bash
  winget install --id Git.Git -e --source winget
  ```
</details>

If you do not have `uv` installed, run the following command.

<details>
  <summary> Install using Homebrew (Darwin) </summary>

  ```bash
  brew install uv
  ```
</details>

<details>
  <summary>
    Install using standalone installer (Darwin, Linux, or Windows Subsystem for Linux [WSL])
  </summary>

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
</details>

<details>
  <summary> Install using Winget (Windows Powershell) </summary>

  ```bash
  winget install --id=astral-sh.uv -e
  ```
</details>

Once you have `git` distributed version control system installed, you can
clone the current repository and  install any version of Python above version
3.9 for this project. The following commands help you set up and activate a
Python virtual environment where `uv` can download project dependencies from the `PyPI`
open-sourced registry defined under `pyproject.toml` file.

<details>
  <summary> Set up environment and synchronize project dependencies </summary>

  ```bash
  git clone git@github.com:ta007403/LNbits-Lightning-Transfer.git
  cd LNbits-Lightning-Transfer
  uv venv --python 3.9.6
  source .venv/bin/activate
  uv sync --dev
  ```
</details>

### Getting started

Once you have virtual environment set up, install project dependencies with the following
command:

```bash
uv sync
```

<details>
  <summary> Sample output of successful dependency installation </summary>

  ```bash
  $ uv sync
  > Resolved 6 packages in 2ms
  > Prepared 1 package in 146ms
  > Installed 6 packages in 6ms
  >  + certifi==2025.7.14
  >  + charset-normalizer==3.4.2
  >  + idna==3.10
  >  + lnbitstx==0.0.1 (from file:///.../.../.../lnbitstx)
  >  + requests==2.32.4
  >  + urllib3==2.5.0
  ```
</details>

Edit the given script by changing the following parameters:
```python
LNBITS_API_KEY = "xxx" 
LNBITS_API_URL = "xxx"
```

As seen on attached image here:

![image](https://github.com/user-attachments/assets/3e06cc1e-5ba7-4236-838a-5cbc8dfbdc86 =993x523)

Then run the given script by targeting script-file with `python` command:

```bash
python LN_Send_Sat_To_WOS.py {{address}} {{amount}}
```

<details>
  <summary> Sample output for successful script via `python` command </summary>

  ```bash
  $ python LN_Send_Sat_to_WOS.py lyricalweather78@walletofsatoshi.com 90
  > ⚡ Getting invoice for 90 sats to lyricalweather78@walletofsatoshi.com...
  > ⚡ Paying invoice...
  > 🔥 Error: Invalid URL 'xxx': No scheme supplied. Perhaps you meant https://xxx?
  ```
</details>

Or, similarly you can also use `lnbitstx` command on your terminal emulator installed
after synchronization of this project's dependencies as well:

```bash
lnbitstx {{address}} {{amount}}
```

<details>
  <summary> Sample output for successful script via `lnbitstx` command </summary>

  ```bash
  $ lnbitstx lyricalweather78@walletofsatoshi.com 90
  > ⚡ Getting invoice for 90 sats to lyricalweather78@walletofsatoshi.com...
  > ⚡ Paying invoice...
  > 🔥 Error: Invalid URL 'xxx': No scheme supplied. Perhaps you meant https://xxx?
  ```
</details>

## Contributions

### Prerequisites

Install development dependencies using `uv` command

```bash
uv sync --dev
```

<details>
  <summary> Sample output of successfully installing development dependencies </summary>

  ```bash
  $ uv sync --dev
  > Resolved 13 packages in 8ms
  >       Built lnbitstx@ file:///.../.../.../lnbitstx
  > Prepared 1 package in 349ms
  > Installed 13 packages in 20ms
  >  + certifi==2025.7.14
  >  + charset-normalizer==3.4.2
  >  + idna==3.10
  >  + lnbitstx==0.0.1 (from file://.../.../.../lnbitstx)
  >  + mypy==1.17.1
  >  + mypy-extensions==1.1.0
  >  + pathspec==0.12.1
  >  + requests==2.32.4
  >  + ruff==0.12.7
  >  + tomli==2.2.1
  >  + types-requests==2.32.4.20250611
  >  + typing-extensions==4.14.1
  >  + urllib3==2.5.0
  ```
</details>

Run static type-checking using `mypy` with the following command:

```bash
mypy .
```

<details>
  <summary> Sample output of successfully type-checking project </summary>

  ```bash
  $ mypy .
  > Success: no issues found in 1 source file
  ```
</details>

Run project-wide formatting using `ruff` with the following command:

```bash
ruff format .
```

<details>
  <summary> Sample output of successfully formatting project </summary>

  ```bash
  $ ruff format .
  > 1 file reformatted
  ```
</details>

Run linting / checking sourcecode for stylistic errors with the following `ruff` command:

```bash
ruff check .
```

<details>
  <summary> Sample output of successfully linting project </summary>

  ```bash
  $ ruff check .
  > All checks passed!
  ```
</details>
