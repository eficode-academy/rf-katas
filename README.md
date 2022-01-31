# Robot Framework katas

## Requirements

In this series of exercises we're going to run several automated tests against web application. To do
that we're going to need to have the following items installed:

- Python (version 3.7 or newer): https://www.python.org/downloads/
  - Remember to add Python folder to PATH environment variable.
- Pip for Python 3
  - Windows: https://www.howtogeek.com/197947/how-to-install-python-on-windows/
  - Linux: `sudo apt-get install python3-pip && pip3 install --upgrade pip`
  - macOS: `brew install python` pip is already included
- Node.js (version 12 or newer): https://nodejs.org/en/download/
- System under test
  - Open a new terminal window, change directory to this repository root folder and run the application
    with: `python server/server.py`

### Recommended

- In order to make installing with pip easier, use virtualenv (https://virtualenv.pypa.io/en/latest/)
  - Short instruction to virtualenv use

    ```shell
    pip install virtualenv --user
    virtualenv <choose_a_folder_name>
    source <chosen_folder_name>/bin/activate
    ```

## Get started

After you have installed the requirements check the [Getting started exercise](exercises/00-getting-started.md) and proceed with the exercises.
