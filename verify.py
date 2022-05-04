import sys
import os
from importlib import import_module

EXERCISES = {
    0: import_module("setup.verify_env"),
    1: import_module("setup.01-manual_testing"),
    2: import_module("setup.02-robot_syntax"),
    3: import_module("setup.03-keywords_and_variables"),
    4: import_module("setup.04-setups_and_teardowns"),
    5: import_module("setup.05-negative_testing"),
    6: import_module("setup.06-resource_files"),
    7: import_module("setup.07-test_template")
}

def main(exercise):
    try:
        module = EXERCISES[int(exercise)]
    except:
        print(f"{exercise} code doesn't exists, use the following: {', '.join([str(key) for key in EXERCISES.keys()])}")
        sys.exit(1)
    module.main()

if __name__ == "__main__":
    main(sys.argv[1])