import sys
import subprocess
from pathlib import Path
from pip._internal.utils.misc import get_installed_distributions

IS_CHROME = False
IS_FIREFOX = False
ROOT_FOLDER = Path('.', 'setup')
SMOKE_TEST_SUITE = ROOT_FOLDER / "verify_setup.robot"

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
    if not "robotframework-seleniumlibrary" in pip_packages:
        print("Install SeleniumLibrary: pip install robotframework-seleniumlibrary")
        sys.exit(1)
    
def check_rflint_package():
    pip_packages = get_pip_packages()
    if not "robotframework-lint" in pip_packages:
        print("Install Robot Framework linter: pip install robotframework-lint")
        print("Linter tool is required for exercise verification")
        sys.exit(1)

def check_smoke_suite_location():
    if not SMOKE_TEST_SUITE.is_file():
        print("File not located, please run from root folder of the exercises")
        print(SMOKE_TEST_SUITE)
        sys.exit(1)

def evaluate_environment():
    try:
        subprocess.run(["robot", "-v", "BROWSER:ff", "-d", "setup", SMOKE_TEST_SUITE], check=True)
        IS_FIREFOX = True
    except subprocess.CalledProcessError:
        IS_FIREFOX = False
    try:
        subprocess.run(["robot", "-v", "BROWSER:gc", "-d", "setup", SMOKE_TEST_SUITE], check=True)
        IS_CHROME = True
    except subprocess.CalledProcessError:
        IS_CHROME = False
    if not IS_CHROME and not IS_FIREFOX:
        print("Setup webdriver based on the instructions for Firefox OR Chrome")
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

    