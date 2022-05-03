import sys
import os
from importlib import import_module

EXERCISES = {
    "00": import_module("setup.verify_env"),
    "01": import_module("setup.01-manual_testing"),
    "02": import_module("setup.02-robot_syntax"),
    "03": import_module("setup.03-keywords_and_variables"),
    "04": import_module("setup.04-setups_and_teardowns"),
    "05": import_module("setup.05-negative_testing"),
    "06": import_module("setup.06-resource_files"),
    "07": import_module("setup.07-test_template")
}

def main(exercise):
    os.environ["PYTHONPATH"]="setup" # needed for windows, otherwise we will get error No module named 'static'
    if not exercise in EXERCISES:
        print(f"{exercise} code doesn't exists, use the following: {', '.join(EXERCISES.keys())}")
        sys.exit(1)
    module = EXERCISES[exercise]
    module.main()

if __name__ == "__main__":
    main(sys.argv[1])