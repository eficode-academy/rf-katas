import sys
import os
import subprocess
from pathlib import Path
import importlib.util

SETUP_DIRECTORY = Path(__file__).resolve().parent

IS_CHROME = False
IS_FIREFOX = False
SMOKE_TEST_SUITE = os.path.join(SETUP_DIRECTORY, "verify_setup.robot")

def check_robot_framework_package():
    if importlib.util.find_spec("robot") is None:
        print("Install Robot Framework: pip install robotframework")
        sys.exit(1)

def check_browser_library_package():
    if importlib.util.find_spec("Browser") is None:
        print("Install Browser-library: pip install robotframework-browser")
        sys.exit(1)

def check_rflint_package():
    if importlib.util.find_spec("rflint") is None:
        print("Install Robot Framework linter: pip install robotframework-lint")
        print("Linter tool is required for exercise verification")
        sys.exit(1)

def check_smoke_suite_location():
    if not os.path.isfile(SMOKE_TEST_SUITE):
        print("File not located, please run from root folder of the exercises")
        print(SMOKE_TEST_SUITE)
        sys.exit(1)

def evaluate_environment():
    try:
        subprocess.run(["robot", "-d", str(SETUP_DIRECTORY), SMOKE_TEST_SUITE], check=True)
        BROWSERS_INSTALLED = True
    except subprocess.CalledProcessError:
        BROWSERS_INSTALLED = False
    if not BROWSERS_INSTALLED:
        print("No browser binaries installed. Install them according to the instructions.")
        sys.exit(1)




def main():
    check_robot_framework_package()
    check_browser_library_package()
    check_rflint_package()
    check_smoke_suite_location()
    evaluate_environment()
    print("Setup in perfect condition!")


if __name__ == "__main__":
    main()
