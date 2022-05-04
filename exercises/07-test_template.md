# Test templates

<details>
    <summary>After the previous exercise our <code>invalid_login.robot</code>
    should look something like this</summary>

```robot
*** Settings ***
Library    Browser
Resource    common.resource

*** Variables ***

*** Test Cases ***

Error Page Should Be Visible After Invalid Login With Empty And Space
    Open Browser To Login Page
    Enter Username    ${EMPTY}
    Enter Password    ${SPACE*2}
    Submit Login Form
    Verify That Error Page Is Visible

Error Page Should Be Visible After Invalid Login With Valid Username And Invalid Password
    Open Browser To Login Page
    Enter Username    ${USERNAME}
    Enter Password    asdsadsa
    Submit Login Form
    Verify That Error Page Is Visible

Error Page Should Be Visible After Invalid Login With Invalid Username And Valid Password
    Open Browser To Login Page
    Enter Username    asdsadsa
    Enter Password    ${PASSWORD}
    Submit Login Form
    Verify That Error Page Is Visible

*** Keywords ***

Verify That Error Page Is Visible
    Get Text    body    contains    Error Page
    Get Url    ==    ${URL}/error.html
    Get Title    ==    Error Page
```

</details>

So, basically what most of us did was copy-paste the first test several times, change the test names
and change the entered usernames and passwords. The tests do test different things and work well, but it
doesn't really make sense to copy-paste several lines and modify 2 parameters. Instead, we should use
[test templates](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates).

So far we've been doing so-called workflow tests. Test templates are so-called **data-driven tests**, which are
applicable when you need to run the same test, multiple times, every time with a couple of slightly altered arguments.

## Exercise

- Rename the first test case to `Error Page Is Visible When Using Incorrect Credentials`
and move it from the `Test Cases` table under the `Keywords` table.

The `Error Page Is Visible When Using Incorrect Credentials` keyword starts with a
`Open Browser to Login Page`-keyword. This repeats in every test while it's not really part of the testing.
We can get rid of the repetitive keyword by adding it as `Test Setup` into our `Settings` table. Test setup in
the settings table acts in the same way as the `[Setup]` defined to our valid login test case. However, when
put into the settings table it means the setup is the same for all test cases in the test suite and you don't
need to add `[Setup]` to all test cases individually. The same applies for the `Test Teardown` and `[Teardown]`.

- Add `Test Setup` to your settings table and add `Open Browser To Login Page` as the test setup.
- Remove `Open Browser To Login Page` from your `Error Page Is Visible When Using Incorrect Credentials`.
- Add arguments for username and password for your template keyword.

*Pro-tip:* A keyword can take multiple arguments when separating them with 4 spaces.

<details>

<summary>So now our `Settings` table should look like this</summary>

```robot
*** Settings ***
Library    Browser
Resource    common.resource
Test Setup    Open Browser To Login Page
```

</details>

<details>
<summary>And `Keywords` table like this</summary>

```robot
*** Keywords ***
Verify That Error Page Is Visible
    Get Text    body    contains    Error Page
    Get Url    ==    ${URL}/error.html
    Get Title    ==    Error Page

Error Page Is Visible When Using Incorrect Credentials
    [Arguments]    ${username}    ${password}
    Enter Username    ${username}
    Enter Password    ${password}
    Submit Login Form
    Verify That Error Page Is Visible
```

</details>

Now we've prepared our suite to get ready for data driven tests. Let's add the final piece to the `Settings` table.
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#data-driven-style

- Add `Test Template` to the `Settings` table. Value for this setting should be
`Error Page Is Visible When Using Incorrect Credentials`.
- Remove all your test cases from `invalid_login.robot` test suite.

<details>
<summary>Our `Settings` table should look like this:</summary>

```robot
*** Settings ***
Library    Browser
Resource    common.resource
Test Setup    Open Browser To Login Page
Test Template    Error Page Is Visible When Using Incorrect Credentials
```

</details>

Let's create our very first data driven test case.

So now that we're using the data driven style of creating test case, under test case table we can write
`<name_of_the_test_case>    <username>    <password>`. Like this:

```robot
*** Test Cases ***
#test case name                  #username   #password
Empty Username Empty Password    ${EMPTY}    ${EMPTY}
```

*Note:* the commented line (one starting with `#`) isn't required. It's there merely to server as a
header for the test case table to enhance readability.

- Add a test case followed and on the same line add 4 spaces a username and 4 spaces and password.

Now run `robot robot/invalid_login.robot` command to verify that changes are done correctly.

- Create 4 more test cases with different values for username and password.

## Verification

Once you've implemented all 5 test cases run:

- in Windows: run command `python verify.py 07`
- in macOS/Linux: run command `python3 verify.py 07`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
