import os
import sys

ROBOT_ROOT_PATH = os.path.abspath(os.path.join(".", "robot"))
LOGIN_ROBOT_FILE = os.path.abspath(os.path.join(ROBOT_ROOT_PATH, "login.robot"))
INVALID_LOGIN_ROBOT = os.path.abspath(os.path.join(ROBOT_ROOT_PATH, "invalid_login.robot"))
CURRENT_ENV = os.environ.copy()
if "PYTHONPATH" in CURRENT_ENV:
    CURRENT_ENV["PYTHONPATH"] = f"setup{os.pathsep}" + CURRENT_ENV["PYTHONPATH"]
else:
    CURRENT_ENV["PYTHONPATH"] = f"setup{os.pathsep}"


def normalize(keyword):
    return keyword.strip().title()


def check_running_in_root():
    current_folder = os.getcwd()
    supposed_exercises_folder = os.path.abspath(os.path.join(current_folder, "exercises"))
    supposed_setup_folder = os.path.abspath(os.path.join(current_folder, "setup"))

    in_root = os.path.isdir(supposed_exercises_folder) and os.path.isdir(supposed_setup_folder)
    if not in_root:
        print(f"🚩 Hmm. It looks like the script is running in '{current_folder}' instead of the repo root folder.")
        print("For the verification to work correctly, you need to run the script from the root of the repository ("
              "probably named 'rf-katas').")
        print("Try again, but double-check that you're running the verify script from the repository root.")
        sys.exit(1)
