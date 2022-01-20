# Setups and Teardowns

Robot Framework provides features called _Setup_ and _Teardown_ to help with repetitive parts that
which are required to run the test, but are not necessary _part_ of the tests. In our case such things
would be e.g. opening and closing the browser. More details can be found at
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown.

<details>
    <summary>From our previous exercises our <code>login.robot</code> should look something like this</summary>

```robot
*** Settings ***
Library    Browser

*** Variables ***
${URL} =    http://localhost:7272
${USERNAME} =    demo
${PASSWORD} =    mode

*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    Open Browser To Login Page
    Enter Username    ${USERNAME}
    Enter Password    ${PASSWORD}
    Submit Login Form
    Verify That Welcome Page Is Visible

*** Keywords ***

Open Browser To Login Page
    New Browser    headless=${FALSE}
    New Page    ${URL}

Enter Username
    [Arguments]    ${username}
    Fill Text    id=username_field    ${username}

Enter Password
    [Arguments]    ${password}
    Fill Secret    id=password_field    ${password}

Submit Login Form
    Click    id=login_button

Verify That Welcome Page Is Visible
    Get Text    body    contains    Welcome Page
    Get Url    ==    ${URL}/welcome.html
    Get Title    ==    Welcome Page
```

</details>

## Test Setup

As was defined in SUT features, the logout link is only visible after successful login.
Create a new test case that first logins and then clicks the logout link, since we want to
make our test cases so that they can be run individually. Remember to create a keyword to
verify the login form visibility.

Name the new test case `Login Form Should Be Visible After Successful Logout`.

After implementing the new test case run both of the test cases with command
`robot --randomize tests robot/login.robot` to make sure that they're not executed in order all the
time. This helps to ensure that all tests pass regardless of what order they are run in. Check
`robot -h` for more info.

You may have noticed that you just copy-pasted the `Welcome Page Should Be Visible After Successful Login`
test steps, then proceeded to click the link and verify that login form is visible.

The new test case is now quite long, which makes it harder to understand. It should be easier to
comprehend the main point of the test for people reading the steps (it also should be clear from the
test case name). To improve the readability, add a proper test setup for the test case.

To do that let's create new keyword called `Do Successful Login` with following content:

```robot
Do Successful Login
    Open Browser To Login Page
    Enter Username
    Enter Password
    Submit Login Form
```

Now refactor both test cases by adding that part to test setup with `[Setup]` option.

Now the test cases should look something like this:

```robot
Welcome Page Should Be Visible After Successful Login
    [Setup]    Do Successful Login
    # rest of the implementation

Login Form Should Be Visible After Successful Logout
    [Setup]    Do Successful Login
    # rest of the implementation
```

*Tip:* `#` starts a comment line for Robot Framework. Nothing after it will be executed.

Existence of `Setup` indicates to the test case reader, that there is some precondition before our actual test execution.

## Test Teardown

Teardown works similarly to Setup with the main difference being that it will be executed after the
main part of the test has run. Teardowns are _always_ run, regardless whether the test succeeds or
fails.

Similarly to the `[Setup]`, a teardown would be defined with a `[Teardown]` option in the end of the
test case. So for example, if we would want to ensure that the browser is closed after the test, we
could add a `[Teardown]    Close Browser` to the end. This would run the `Close Browser` keyword every
time after the test. In our case it is _not necessary_, as the Browser-library closes all open browsers
by default after each test case. (This setup can be changed with one of the Browser's
[import arguments](https://marketsquare.github.io/robotframework-browser/Browser.html#Importing).)

To ensure that changes are done in right manner run:

- Windows: double-click the `04-setups_and_teardowns.cmd`
- Linux/macOS: run `./exercises/verify/04-setups_and_teardowns.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
