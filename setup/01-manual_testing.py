import os
import sys
import re
from static import LOGIN_ROBOT_FILE

def check_file_exists():
    if not os.path.isfile(LOGIN_ROBOT_FILE):
        print("login.robot not found under {}, please create one".format(LOGIN_ROBOT_FILE))
        sys.exit(1)

def check_content():
    is_open_browser = False
    is_url = False
    is_password = False
    is_username = False
    data = None
    with open(LOGIN_ROBOT_FILE, "r") as f:
        data = f.readlines()
    for line in data:
        lowered_line = line.lower()
        if "open browser" in lowered_line:
            is_open_browser = True
        elif re.search("localhost:7272", lowered_line):
            is_url = True
        elif "username" in lowered_line:
            is_username = True
        elif "password" in lowered_line:
            is_password = True
    if is_open_browser and is_url and is_password and is_username:
        print("Ready to proceed!")
    else:
        print("Not quite there yet! Did remember browser, username, password or perhaps missing url?")
        sys.exit(1)

def main():
    check_file_exists()
    check_content()


if __name__ == "__main__":
    main()
