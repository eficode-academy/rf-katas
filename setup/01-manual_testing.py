import os
import sys
from static import LOGIN_ROBOT_FILE

def check_file_exists():
    if not os.path.isfile(LOGIN_ROBOT_FILE):
        print(f"Hmm. I don't see your 'login.robot' file. I was expecting to see it at, '{LOGIN_ROBOT_FILE}'")
        print("Double-check that it's in the right place and named correctly and try again.")
        sys.exit(1)

def demonstrate_our_solution():
    print("Nice job!")
    print("If you'd like to compare answers, here's our solution:")
    print("""
    Open browser
    Navigate to localhost:7272
    Enter username
    Enter password
    Submit login form
    Check that welcome page text is visible
    """)

def main():
    check_file_exists()
    demonstrate_our_solution()
    print("Ready to proceed!")



if __name__ == "__main__":
    main()
