import sys
import subprocess
from setup.static import INVALID_LOGIN_ROBOT, CURRENT_ENV

def run_linting():
    try:
        subprocess.run(["rflint", "-A", "setup/07-test_template.args", INVALID_LOGIN_ROBOT], check=True, env=CURRENT_ENV)
    except subprocess.CalledProcessError:
        print("Linting failed, check the results, fix and run again")
        sys.exit(1)

def run_test():
    try:
        subprocess.run(["robot", "--randomize", "tests", "-d", "setup", INVALID_LOGIN_ROBOT], check=True)
    except subprocess.CalledProcessError:
        print("Test run failed, check the results, fix and run again")
        sys.exit(1)

def main():
    run_linting()
    run_test()
    print("Ready to proceed!")

if __name__ == "__main__":
    main()
