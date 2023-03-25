# Setups and Teardowns

Robot Framework provides features called _Setup_ and _Teardown_ to help with repetitive parts
which are required to initialize or disassemble the tests, but are not necessary _part_ of them. In
our case such things would be e.g. opening and closing the browser, and perhaps in some cases, logging
out.

More details on setup and teardown can be found from the corresponding
[Test setup and teardown](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown)-documentation.

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

## Exercise

As was defined in SUT features, the logout link is only visible after a successful login. So far we
have not made any tests to validate that logging out works as expected, but perhaps we should?

Create a new test case that first logins and then clicks the logout link, since we want to
make our test cases so that they can be run individually. Remember to create a keyword to
verify the login form visibility.

- Create a new test case called `Login Form Should Be Visible After Successful Logout`.
- Copy the steps of `Welcome Page Should Be Visible After Successful Login` test case to your new test case.
- Create 2 new keywords and corresponding logic to those keywords.
    - `Do Successful Logout`
    - `Verify That Login Page Is Visible`
- Call your new keywords in your new test case.

After implementing the new test case run both of the test cases with command
`robot --randomize tests robot/login.robot` to make sure that they're not executed in order all the
time. This helps to ensure that all tests pass regardless of what order they are run in. Check
`robot -h` for more info.

### Test Setup

The new test case is now quite long, which makes it harder to understand. It should be as easy as possible
to comprehend the main point of the test for people reading the steps (it also should be clear from the
test case name). Let's improve the readability by adding a proper test setup for the test case.

Existence of a `Setup` indicates to the test case reader, that there is some precondition before our
actual test execution.

- Create a new keyword called `Do Successful Login` with following content:

    ```robot
    Do Successful Login
        Open Browser To Login Page
        Enter Username
        Enter Password
        Submit Login Form
    ```

Then we can refactor both test cases by adding that part to test setup with `[Setup]` option.

- Add a `[Setup]` as the first step of your logout test case.
- Add 4 spaces and a `Do Successful Login` call after the setup (on the same line).

<details>
    <summary>Now the test cases should look like this</summary>

```robot
Login Form Should Be Visible After Successful Logout
    [Setup]    Do Successful Login
    # rest of the implementation
```

*Pro-tip:* `#` starts a comment line for Robot Framework. Nothing after it (on that line) will be executed.

</details>

### Test Teardown

Teardown works similarly to setup, with the main difference being that it will be executed after the
main part of the test has run. If teardowns are defined, they're _always_ run, regardless whether the
test succeeds or fails mid-execution.

As explained in the introduction to this exercise, one of the main ideas of setups and teardowns is
wrapping the non-testing parts into them. Neither setups nor teardowns have to be the same in every
single test case, even within a suite (which was simply a single file with one or more test cases).
We have two tests that test two different things.

Perhaps we could add a teardown to the first test case which the user out after the test. (Note that
the second test case already does a logout _as part of the test_, so the teardown would not be needed
in that.)

The teardown is defined a similar way as was setup, using the `[Teardown]` option.

- Add a `[Teardown]` to your `Welcome Page Should Be Visible After Successful Login` test case.
- Call `Do Successful Logout` as the teardown for that test case.

## Verification

To ensure that changes are done in right manner run:

- in Windows: run command `python verify.py 04`
- in macOS/Linux: run command `python3 verify.py 04`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
