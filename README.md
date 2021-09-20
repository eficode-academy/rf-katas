# Robot Framework katas

## Requirements

In this series of exercises we're going to run several automated tests againts web application. To do that we're going to need to have the following items installed:

- Python 3: https://www.python.org/downloads/
  - Remember to add Python folder to PATH environment variable.
- Pip for Python 3
  - Windows: https://www.howtogeek.com/197947/how-to-install-python-on-windows/
  - Linux: `sudo apt-get install python3-pip && pip3 install --upgrade pip`
  - MacOS: `brew install python` pip is already included
- Browser
  - Chrome and chromedriver: https://chromedriver.chromium.org/downloads
  - Or Firefox and geckodriver: https://github.com/mozilla/geckodriver/releases
- System under test
    - Open a new terminal window, change directory to this repository root folder and run the application with:
       -  `python server/server.py`

Recommendations:
  - In order to make installing with pip easier, use virtualenv (https://virtualenv.pypa.io/en/latest/)
    - Short instruction to virtualenv use
    ```
    pip install virtualenv --user
    virtualenv <choose_a_folder_name>
    source <chosen_folder_name>/bin/activate`
    ```
  - use webdrivermanager to manage browser drivers
    ```
    pip install webdrivermanager
    webdrivermanager firefox
    webdrivermanager chrome
    ```
    
Protip (if not using webdrivermanager): Add the chromedriver or geckodriver (after download) to a location that is in PATH environment variable. To see what folders are included you can use
  - MacOS/Linux: in terminal run command: `echo $PATH`
  - Windows:
    - in Command Prompt run command: `echo %PATH`
    - in PowerShell run command: `echo $env:path`

## Get started

After you have installed the requirements check the [Getting started exercise](exercises/00-getting-started.md) and proceed with the exercises
