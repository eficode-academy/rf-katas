# Manual testing

Manual testing is usually a part of test automation. We need to know what the steps are 
before we can automate them.

Let us first go through our System Under Testing (SUT) before we proceed.

## System Under Testing (SUT)

Our SUT is a simple web application that is running on `http://localhost:7272`.

### Features

- The index page contains a login form
  - Username: `demo`
  - Password: `mode`
  - Submit login form button
- After successful login, the user is redirected to the welcome page.
  - User can log out after successful login and will be redirected to the login page.
- After incorrect login credentials, the user is redirected to the error page.

## Exercise

How would you manually test the successful login use case?

- In the root directory of the rf-katas project create a `robot` folder.
- Inside it add a text file, call it `login.robot` (note that `.robot` is the extension, not `.txt`).
- Write line by line, all the steps that you would need to perform if you were manually testing the login feature.

## Verify your solution

After you've added the steps that you think are needed to manually test the login feature, run:

- in Windows: run command `python verify.py 01`
- in macOS/Linux: run command `python3 verify.py 01`

If the final output is `Ready to proceed!` then you're good to go! Otherwise, check the output to see what is wrong.

When you're ready, move on to the [next section](02-robot-syntax.md).