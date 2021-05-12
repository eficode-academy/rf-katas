import os
ROBOT_ROOT_PATH = os.path.abspath(os.path.join(".", "robot"))
LOGIN_ROBOT_FILE = os.path.abspath(os.path.join(ROBOT_ROOT_PATH, "login.robot"))
INVALID_LOGIN_ROBOT = os.path.abspath(os.path.join(ROBOT_ROOT_PATH, "invalid_login.robot"))

def normalize(keyword):
    return keyword.strip().title()