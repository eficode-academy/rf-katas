import sys
import subprocess as sp

def main(exercise):
    if not exercise.startswith("0") or exercise == "0":
        exercise = "0" + exercise
    if sys.platform in ["linux", "darwin"]:
        sp.call(f"./exercises/verify/{exercise}-*.sh", shell=True)
    else:
        sp.call(f"exercises\\verify\\{exercise}-*.cmd", shell=True)

if __name__ == "__main__":
    main(sys.argv[1])