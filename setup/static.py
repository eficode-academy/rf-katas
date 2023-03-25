import os
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