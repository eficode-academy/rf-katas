# Resource files

In the previous exercise you might have ended up copy-pasting the
existing test case from `login.robot` test suite to `invalid_login.robot`.

<details>
    <summary>So your <code>invalid_login.robot</code> could look something like this</summary>

```robot
*** Settings ***
Library    Browser

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

*** Keywords ***

Open Browser To Login Page
    New Browser    headless=${FALSE}
    New Page    ${URL}

Enter Username
    [Arguments]    ${username}
    Fill Text    id=username_field    ${username}

Enter Password
    [Arguments]    ${password}
    Fill Secret    id=password_field    $password

Submit Login Form
    Click    id=login_button

Verify That Error Page Is Visible
    Get Text    body    contains    Error Page
    Get Url    ==    ${URL}/error.html
    Get Title    ==    Error Page
```

</details>

As you noticed, we now have duplication in keywords like `Open Browser To Login Page` and `Submit Login Form`.

Usually we don't want to repeat ourselves that much, since it makes maintenance much harder.
To ease out maintenance we can use
[resource files](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#resource-and-variable-files).

## Exercise

The biggest difference between resource files and test suite files is that in a resource file you
don't have the `*** Test Cases ***` or `*** Tasks ***` table. It is
[recommended](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#taking-resource-files-into-use)
to use a `.resource` extension with resource files (instead of the otherwise used `.robot`). This is
just for separating resource files from test files. The functionality will remain the same.

- Create our `common.resource` file under `robot`.
- Cross-check between `login.robot` and `invalid_login.robot` and find the duplicate keywords.
    - Move all duplicate keywords to `common.resource` and remove them from `login.robot` and `invalid_login.robot`.

Now run the command `robot robot` to run all suites. You may notice some errors.

```text
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

Why is that? We have the keywords in our `common.resource`, right?

The reason is the same that we had with non `Builtin` Libraries. We need to tell the Robot Framework
to use our `common.resource` in our test suite.

That's why you need to add `Resources` four spaces `<resource_name>` to your `*** Settings ***` table in
your test suite file. Resource files can also resource other resource files.

- Add a `Resource` to your `login.robot` to resource your `common.resource`.

<details>
    <summary>Your settings table should look like this</summary>

```robot
*** Settings ***
Library    Browser
Resource    common.resource
```

</details>

Now, when you run `robot robot/login.robot`, the tests should pass again.

- Add missing `Resource` option to `robot/invalid_login.robot` file as well and ensure your tests are passing.
- Create two more test cases that use two different combination of invalid credentials to `invalid_login.robot`.

## Verification

When the tests pass run the following command to ensure that changes are done in right manner run:

- in Windows: run command `python verify.py 06`
- in macOS/Linux: run command `python3 verify.py 06`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
