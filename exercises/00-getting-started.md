# Getting started

In this section we'll 
 - install Robot Framework
 - install some needed test libraries
 - prepare the environment for web UI testing

## Terminology

In this section, you will see a lot of Python, operating system, and Robot Framework related jargon
which might be confusing to some. So before you go further, let's clarify some terminology that is
used frequently in this ecosystem.

- *pip* — Python package manager; this is a tool that is needed to install Robot Framework and needed test libraries.
- *shell* — The shell is the command interpreter in an operating system such as Unix or GNU/Linux, it is a program that executes other programs. A.K.A.: Terminal, Command Prompt.
- *bat / batch file / cmd* — A batch file is a script file in DOS, OS/2 and Microsoft Windows. It consists of a series of commands to be executed by the command-line interpreter, stored in a plain text file.
- *`robot`* — The command line tool that allows the user to run Robot Framework test cases and tasks. 
- *test suite* — A group of test cases. In Robot Framework, a test suite is contained in single file.
- *keyword* — A defined step; similar to a function in programming. There are [built-in keywords](https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst#library-keywords) or you can [define your own](https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst#user-keywords).
- *arguments*  — Values that are given to keywords. Also known as parameters.

## Get the Repository

Clone the repository or download and extract the repository ZIP to your local machine. All exercises will be completed using the
local copy of the repo.

![Clone the repository](img/clone_repo.png)

## Install Robot Framework

### Using `pip`
In order to run Robot Framework test cases we're going to need install Robot Framework. We install this by
using `pip`. Usually you install something by calling `pip3 install <package_name>`, but if you are
using a virtual environment, or have an alias defined, you can try `pip install <package_name>` instead.

### Installing Robot Framework
Run `pip3 install robotframework`

To check that it was installed, run the `robot --help` command. The output should include Robot Framework version number and some other helpful stuff,
including the command line options (which are also available [here](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#all-command-line-options)).

### Consistency Helper
In order to ensure that you've done exercises as expected let's install the "robotframework-lint"
tool. A linting tool is a lightweight static analysis tool to verify that you and your team are doing
your code consistently.

To install the linter, run `pip3 install robotframework-lint`

### Testing in the Browser
Robot Framework can test anything if you give it the right library. To run automated test cases for web UIs, we'll use the "Browser" library.

To install this "Browser" library, run `pip3 install robotframework-browser`

After the installation has completed successfully,
the library has to be initialized by running `rfbrowser init`—you'll need [Node.js installed](https://nodejs.org/en/download/). It will take a a minute or two to run the command.

## Start server

In order to run the exercises in this training, you need to start the demo app. You can start the server
by running `python3 server/server.py` in your terminal/command prompt. Your terminal or command prompt is
now occupied with running the server, which means you need to open another terminal/command prompt to run
your tests.

After the server has started it will be running in http://localhost:7272.

## Verify installation

Verify setup by running:

- in Windows: double click 00-verify_setup.cmd
- in macOS/Linux: run command `./exercises/verify/00-verify_setup.sh`

> If you run into an `ImportError: cannot import name 'get_installed_distributions' from 'pip._internal.utils.misc'` error, the workaround is to downgrade your pip by running, `pip3 install pip==21.2.4`. See [issue #20](https://github.com/eficode-academy/rf-katas/issues/20) for details.

This should take a few seconds. If the output of the script ends with `Setup in perfect condition!`
we're good to go.

Otherwise, check the output and fix the missing packages.
