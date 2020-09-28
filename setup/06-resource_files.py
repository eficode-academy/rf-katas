import os
import sys
import subprocess
from static import ROBOT_ROOT_PATH, INVALID_LOGIN_ROBOT, LOGIN_ROBOT_FILE

RESOURCE_FILE = os.path.join(ROBOT_ROOT_PATH,'resource.robot')


def check_file_exists():
    if not os.path.isfile(RESOURCE_FILE):
        print("resource.robot not found under {}, please create one".format(RESOURCE_FILE))
        sys.exit(1)

def run_linting():
    try:
        subprocess.run(["rflint", "-A", "setup/06-resource_files.args", INVALID_LOGIN_ROBOT, LOGIN_ROBOT_FILE, RESOURCE_FILE], check=True)
    except subprocess.CalledProcessError:
        print("Linting failed, check the results, fix and run again")
        sys.exit(1)

def run_test():
    try:
        subprocess.run(["robot", "--randomize", "tests", "-d", "setup", INVALID_LOGIN_ROBOT, LOGIN_ROBOT_FILE], check=True)
    except subprocess.CalledProcessError:
        print("Test run failed, check the results, fix and run again")
        sys.exit(1)

def main():
    check_file_exists()
    run_linting()
    run_test()
    print("Ready to proceed!")

if __name__ == "__main__":
    main()
