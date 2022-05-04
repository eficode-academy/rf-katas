# Manual testing

Manual testing is usually a part of test automation. We need to know the steps that are then going to
be automated.

Let us first go through our System Under Testing (SUT) before we proceed.

## System Under Testing (SUT)

Our SUT is simple web application that is running at localhost:7272 address.

Features:

- Index page contains login form
  - Username: `demo`
  - Password: `mode`
  - Submit login form button
- After successful login the user is redirected to the welcome page
  - User can log out after successful login and will be redirected to the login page
- After incorrect login credentials the user is redirected to the error page

## Exercise

How would you manually test the successful login use case?

- In the root directory of the rf-katas project create a `robot` folder.
- Inside it add a text file, call it `login.robot` (note that `.robot` is the extension, not `.txt`).
- Write line by line, all the steps that you would need to perform if you were manually testing the login feature.

## Verify your results

After you've added steps that you think are needed to manually test login feature run:

- in Windows: run command `python verify.py 01`
- in macOS/Linux: run command `python3 verify.py 01`

If the output is `Ready to proceed!` then you're good to go! Otherwise, the check the output about what is missing?
