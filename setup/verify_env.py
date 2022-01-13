import sys
import os
import subprocess
from pathlib import Path
from pip._internal.utils.misc import get_installed_distributions

SETUP_DIRECTORY = Path(__file__).resolve().parent

IS_CHROME = False
IS_FIREFOX = False
SMOKE_TEST_SUITE = os.path.join(SETUP_DIRECTORY, "verify_setup.robot")

def get_pip_packages():
    pip_packages = []
    packages = get_installed_distributions()
    for package in packages:
        pip_packages.append(package.project_name)
    return pip_packages

def check_robot_framework_package():
    pip_packages = get_pip_packages()
    if not "robotframework" in pip_packages:
        print("Install Robot Framework: pip install robotframework")
        sys.exit(1)

def check_selenium_library_package():
    pip_packages = get_pip_packages()
    if not "robotframework-browser" in pip_packages:
        print("Install Browser-library: pip install robotframework-browser")
        sys.exit(1)

def check_rflint_package():
    pip_packages = get_pip_packages()
    if not "robotframework-lint" in pip_packages:
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
    check_selenium_library_package()
    check_rflint_package()
    check_smoke_suite_location()
    evaluate_environment()
    print("Setup in perfect condition!")


if __name__ == "__main__":
    main()
