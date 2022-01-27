# Setups and Teardowns

Robot Framework provides features called _Setup_ and _Teardown_ to help with repetitive parts
which are required to initialize or disassemble the tests, but are not necessary _part_ of them. In
our case such things would be e.g. opening and closing the browser, and perhaps in some cases, logging
out.

More details on setup and teardown can be found from the corresponding [Test setup and teardown](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown)-documentation.

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

As was defined in SUT features, the logout link is only visible after a successful login. So far we
have not made any tests to validate that logging out works as expected, but perhaps we should?

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

## Test Setup

The new test case is now quite long, which makes it harder to understand. It should be as easy as possible
to comprehend the main point of the test for people reading the steps (it also should be clear from the
test case name). Let's improve the readability by adding a proper test setup for the test case.

To do that we need to create a new keyword called `Do Successful Login` with following content:

```robot
Do Successful Login
    Open Browser To Login Page
    Enter Username
    Enter Password
    Submit Login Form
```

Then we can refactor both test cases by adding that part to test setup with `[Setup]` option.

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

Existence of `Setup` indicates to the test case reader, that there is some precondition before our
actual test execution.

## Test Teardown

Teardown works similarly to setup, with the main difference being that it will be executed after the
main part of the test has run. If teardowns are defined, they're _always_ run, regardless whether the
test succeeds or fails mid-execution.

As explained in the introduction to this exercise, one of the main ideas of setups and teardowns is
wrapping the non-testing parts into them. Neither setups nor teardowns have to be the same in every
single test case, even within a suite (which was simply a single file with one or more test cases).
We have two tests that test two different things.

Perhaps we could add a teardown to the first test case which the user out after the test. (Note that
the second test case already does a logout *as part of the test*, so the teardown would not be needed
in that.)

The teardown is defined a similar way as was setup, using the `[Teardown]` option.

*Tip:* In order to make the `Login Form Should Be Visible After Successful Logout` test work, you've
probably created a `Do Successful Logout` keyword for logging out. Maybe we could utilize
that in the teardown?

To ensure that changes are done in right manner run:

- Windows: double-click the `04-setups_and_teardowns.cmd`
- Linux/macOS: run `./exercises/verify/04-setups_and_teardowns.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
