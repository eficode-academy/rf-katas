# Resource files

In the previous exercise you might have ended up copy-pasting the
existing test case from `login.robot` test suite to `invalid_login.robot`.

<details>
    <summary>So your `invalid_login.robot` could look something like this</summary>

```
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}=    http://localhost:7272
${USERNAME}=    demo
${PASSWORD}=    mode

*** Test Cases ***

Error Page Should Be Visible After Successful Login
    Open Browser To Login Page
    Enter Username    ${EMPTY}
    Enter Password    ${SPACE*2}
    Submit Login Form
    Verify That Error Page Is Visible
    [Teardown]    Close Browser

*** Keywords ***

Open Browser To Login Page
    Open Browser    ${URL}   browser=ff

Enter Username
    [Arguments]    ${username}
    Input Text    id=username_field    ${username}

Enter Password
    [Arguments]    ${password}
    Input Password    id=password_field    ${password}

Submit Login Form
    Click Element    id=login_button

Verify That Error Page Is Visible
    Page Should Contain    Error Page
    Location Should Be    ${URL}/error.html
    Title Should Be    Error Page
```

</details>

As you noticed, we now have duplication in keywords like `Open Browser To Login Page` and `Submit Login Form`.

Usually we don't want to repeat ourselves that much, since it makes maintenance much harder.
To ease out maintenance we can use resource files:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#resource-and-variable-files

The biggest difference between resource files and test suite files is that in a resource file you don't have the
`*** Test Cases ***` or `*** Tasks ***` table.

So let's create our `resource.robot` file under `robot`.

Now do a cross-check between `login.robot` and `invalid_login.robot`. Find the duplicate keywords from
`login.robot` and `invalid_login.robot` and move them to `resource.robot`. Remove these keywords from
`login.robot` and `invalid_login.robot`.

Now run the command `robot robot` to run all suites and you may notice some errors.

```
=============================================================================
Login & Invalid Login
==============================================================================
Login & Invalid Login.Login
==============================================================================
Welcome Page Should Be Visible After Successful Login                 | FAIL |
No keyword with name 'Open Browser To Login Page' found.
------------------------------------------------------------------------------
Login Form Should Be Visible After Successful Logout                   | FAIL |
Setup failed:
No keyword with name 'Open Browser To Login Page' found.
------------------------------------------------------------------------------
Login & Invalid Login.Login                                           | FAIL |
2 critical tests, 0 passed, 2 failed
2 tests total, 0 passed, 2 failed
==============================================================================
Login & Invalid Login.Invalid Login
==============================================================================
Error Page Should Be Visible After Successful Login                   | FAIL |
No keyword with name 'Open Browser To Login Page' found.
------------------------------------------------------------------------------
Login & Invalid Login.Invalid Login                                   | FAIL |
1 critical test, 0 passed, 1 failed
1 test total, 0 passed, 1 failed
==============================================================================
Login & Invalid Login                                                 | FAIL |
3 critical tests, 0 passed, 3 failed
3 tests total, 0 passed, 3 failed
==============================================================================
```

Why is that? We've it in our `resource.robot`, right?

The reason is the same that we had with non `Builtin` Libraries. We need to tell the Robot Framework
to use our `resource.robot` in our test suite.

That's why you need to add `Resources` 4 spaces `<resource_name>` to your `*** Settings ***` table in
your test suite file. Resource files can also resource other resource files.

Let's modify the `login.robot` settings table by adding the `Resource` option there.

```
*** Settings ***
Library    SeleniumLibrary
Resource    resource.robot
```

Now, when you run `robot robot/login.robot`, the tests should pass again.

Add missing `Resource` option to `robot/invalid_login.robot` file as well and ensure your tests are passing.

Create 2 more test cases that uses 2 different combination of invalid credentials to `invalid_login.robot`.

When the tests pass run the following command to ensure that changes are done in right manner run:

  - Windows: double click the `06-resource_files.cmd`
  - Linux/macOS: run `./verify/06-resource_files.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise check the output and fix, rerun.
