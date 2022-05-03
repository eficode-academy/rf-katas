import os
import sys
import re
from setup.static import LOGIN_ROBOT_FILE

def check_file_exists():
    if not os.path.isfile(LOGIN_ROBOT_FILE):
        print(f"login.robot not found under {LOGIN_ROBOT_FILE}, please create one")
        sys.exit(1)

def check_content():
    is_browser = False
    is_url = False
    is_password = False
    is_username = False
    is_login = False
    is_welcome = False
    data = None
    with open(LOGIN_ROBOT_FILE, "r") as f:
        data = f.readlines()
    for line in data:
        lowered_line = line.lower()
        if re.search(r"(new|open) (page|browser)", lowered_line):
            is_browser = True
        elif re.search(r"localhost:7272", lowered_line):
            is_url = True
        elif "username" in lowered_line:
            is_username = True
        elif "password" in lowered_line:
            is_password = True
        elif "click" in lowered_line or "login" in lowered_line:
            is_login = True
        elif "welcome" in lowered_line:
            is_welcome = True
    if is_browser and is_url and is_password and is_username and is_login and is_welcome:
        print("Ready to proceed!")
    else:
        print("Not quite there yet! Did you remember browser, username, password or perhaps missing url? Did you verify your login succeeded?")
        sys.exit(1)

def main():
    check_file_exists()
    check_content()


if __name__ == "__main__":
    main()
