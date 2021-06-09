# Manual testing

Manual testing is usually a part of test automation. We need to know the steps that are then going to be automated.

Let us first go through our System Under Testing (SUT) before we proceed.

## System Under Testing (SUT)

Our system under testing is simple web application that is running in localhost:7272 address.

Features:
  - index page contains login form
    - username: demo
    - password: mode
    - submit login form button
  - After successful login the user is redirected to welcome page
    - User can logout after successful login and will be redirected to login page
  - After incorrect login credentials the user is redirected to error page

## Exercise 1

How would you test the successful login feature?

Create a file called `login.robot` under `robot` folder.

Write needed steps line by line that you would perform if you would manually test the login feature.

## Verify your results

After you've added steps that you think are needed to manually test login feature run:

  - Windows: double click `01-manual_testing.cmd`
  - Linux/macOS: `./exercises/verify/01-manual_testing.sh`

If the output is `Ready to proceed!` then you're good to go! Otherwise the check the output that what is missing?
