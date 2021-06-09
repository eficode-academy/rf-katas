# Setups and Teardowns

You probably noticed that when you run `robot robot/login.robot`, the automated run will always leave one browser
window open. Wouldn't it be nice if the test automatically closes the browser after the test is executed?
Robot Framework provides setups and teardowns to fix that issue:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown

<details>
    <summary>From our previous exercises our <code>login.robot</code> should look something like this</summary>

```robot
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}=    http://localhost:7272
${USERNAME}=    demo
${PASSWORD}=    mode

*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    Open Browser To Login Page
    Enter Username
    Enter Password
    Submit Login Form
    Verify That Welcome Page Is Visible


*** Keywords ***

Open Browser To Login Page
    Open Browser    ${URL}   browser=ff

Enter Username
    Input Text    id=username_field    ${USERNAME}

Enter Password
    Input Password    id=password_field    ${PASSWORD}

Submit Login Form
    Click Element    id=login_button

Verify That Welcome Page Is Visible
    Page Should Contain    Welcome Page
    Location Should Be    ${URL}/welcome.html
    Title Should Be    Welcome Page
```

</details>

Add `Close Browser` (https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Close%20Browser)
after the last keyword `Verify That Welcome Page is Visible` has been executed. When you run your test,
the browser should close automatically and the test still passes.

Let's make a small error in our test and see what happens. Make a typo in the `Title Should Be` keyword
(inside the `Verify That Welcome Page Is Visible` keyword) parameter to for example `Welcome poge`.

Now run `robot robot/login.robot`. Did the browser close?

The reason why the browser didn't close is because the test failed in the keyword
`Verify That Welcome Page Is Visible`. When a test fails, the execution stops and all keywords that
are after the failing keyword aren't executed anymore. Close the browser manually.

## Test Teardown

Let's modify our test case a bit and let's add a `Teardown` into our test case. Add `[Teardown]` before
`Close Browser` (on the same line, remember to leave 4 spaces between the two), so that our test case
looks like this:

```
Welcome Page Should Be Visible After Sucecsfull Login
    Open Browser To Login Page
    Enter Username
    Enter Password
    Submit Login Form
    Verify That Welcome Page Is Visible
    [Teardown]    Close Browser
```

Now run the `robot robot/login.robot` and what happened? Test case failed,
but the browser was still closed? Open the log.html and you can see that now
the `Close Browser` was executed as a test teardown. A teardown is always executed regardless
to the outcome of the test.

Fix the typo we created to `Title Should Be` inside `Verify That Welcome Page Is Open` keyword
to make the test green once again.

## Test Setup

As was defined in SUT features, the logout link is only visible after successful login.
Create a new test case that first logins and then clicks the logout link, since we want to
make our test cases so that they can be run individually. Remember to create a keyword to
verify the login form visibility.

Name the new test case `Login Form Should Be Visible After Successful Logout`.


*Pro tip.* check the SeleniumLibrary keywords how to click links

After implementing the new test case run both of the test cases with command
`robot --randomize tests robot/login.robot` to make sure that they're not
executed in order all the time. Check `robot -h` for more info.

You may have noticed that you just copy-pasted the `Welcome Page Should Be Visible After Successful Login`
test steps, then proceeded to click the link and verify that login form is visible.

To help people to understand what is the main point of the test case
(also should be clear from the test case name) is to add a proper test setup for the test case.

To do that let's create new keyword called `Do Successful Login` with following content:

```
Do Successful Login
    Open Browser To Login Page
    Enter Username
    Enter Password
    Submit Login Form
```

Refactor the `Login Form Should Be Visible After Successful Logout` test case by adding
that part to test setup with `[Setup]` option.

Now the test case should look something like this:

```
Login Form Should Be Visible After Successful Logout
    [Setup]    Do Successful Login
    # rest of the implementation
```

*Pro tip.*  `#` starts a comment line for Robot Framework

That change indicates the test case reader that there is some precondition before our actual test execution.

To ensure that changes are done in right manner run:

  - Windows: double click the `04-setups_and_teardowns.cmd`
  - Linux/macOS: run `./exercises/verify/04-setups_and_teardowns.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise check the output and fix, rerun.
