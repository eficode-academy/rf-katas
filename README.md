# Robot Framework katas

In this series of exercises we're going to run several automated tests against web application.

## Requirements

To be able to run the exercises the following items need to be installed:

- Python (version 3.8 or newer): https://www.python.org/downloads/
  - Remember to add Python folder to PATH environment variable.
- Pip for Python 3
  - Windows: https://www.howtogeek.com/197947/how-to-install-python-on-windows/
  - Linux: `sudo apt-get install python3-pip && pip3 install --upgrade pip`
  - macOS: `brew install python` pip is already included
- Node.js (version 18 or newer): https://nodejs.org/en/download/
  - Required for [Browser library](https://github.com/MarketSquare/robotframework-browser)

### Recommended

- In order to make installing with pip easier, use python [venv](https://docs.python.org/3/library/venv.html)
  - Short instruction to venv use
    ```shell
    python -m venv <choose_a_folder_name>
    source <chosen_folder_name>/bin/activate # linux, mac
    # or 
    <chosen_folder_name>\Scripts\activate.bat # windows (activate.ps1 on powershell)
    ```

## Get started

After you have installed the requirements check the [Getting started exercise](exercises/00-getting-started.md) and proceed with the exercises.
