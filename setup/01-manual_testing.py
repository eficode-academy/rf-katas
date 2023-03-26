import os
import sys
import re
from setup.static import LOGIN_ROBOT_FILE

def check_file_exists():
    if not os.path.isfile(LOGIN_ROBOT_FILE):
        print(f"❌  Hmm. I don't see your 'login.robot' file. I was expecting to see it at '{LOGIN_ROBOT_FILE}'")
        print("Double-check that it's in the right place and named correctly and try again.")
        sys.exit(1)
    else:
        print("✔️ Found your 'login.robot' file.")

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
        if re.search(r"localhost:7272", lowered_line):
            is_url = True
        if "username" in lowered_line:
            is_username = True
        if "password" in lowered_line:
            is_password = True
        if "click" in lowered_line or "login" in lowered_line:
            is_login = True
        if "welcome" in lowered_line:
            is_welcome = True

    if is_browser:
        print("✔️ Found open browser step.")
    if is_url:
        print("✔️ Found specific URL in steps.")
    if is_username:
        print("✔️ Found mention of username field in steps.")
    if is_password:
        print("✔️ Found mention of password field in steps.")
    if is_login:
        print("✔️ Found login step.")
    if is_welcome:
        print("✔️ Found welcome page step.")

    if is_browser and is_url and is_password and is_username and is_login and is_welcome:
        print("✅  Ready to proceed!")
    else:
        print("❌  Not quite there yet! Did you remember browser, username, password or perhaps missing url? Did you verify your login succeeded?")
        sys.exit(1)

def main():
    check_file_exists()
    check_content()


if __name__ == "__main__":
    main()
