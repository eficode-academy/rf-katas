# Test templates

<details>
    <summary>After the previous exercise our <code>invalid_login.robot</code>
    should look something like this</summary>

```robot
*** Settings ***
Library    Browser
Resource    resource.robot

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
test templates: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates

So far we've been doing so-called workflow tests. Test templates are so-called data driven tests, which are
applicable when you need to run the same test, multiple times, every time with a couple of slightly altered arguments.

Let's get started. Rename the first test case to `Template Error Page Is Visible When Using Incorrect Credentials`
and move it from the `Test Cases` table under the `Keywords` table.

The `Template Error Page Is Visible When Using Incorrect Credentials` keyword starts with a
`Open Browser to Login Page`-keyword. This repeats in every test while it's not really part of the testing.
We can get rid of the repetitive keyword by adding it as `Test Setup` into our `Settings` table.
After that we can delete those the line from `Template Error Page Is Visible When Using Incorrect Credentials`.
A similar addition could be done with teardowns and the `Test Teardown` setting.

Also remember to add arguments for `Template Error Page Is Visible When Using Incorrect Credentials`.

*Tip:* A keyword can take multiple arguments when separating them with 4 spaces.

So now our `Settings` table should look like this:

```robot
*** Settings ***
Library    Browser
Resource    resource.robot
Test Setup    Open Browser To Login Page
```

And `Keywords` table like this:

```robot
*** Keywords ***
Verify That Error Page Is Visible
    Get Text    body    contains    Error Page
    Get Url    ==    ${URL}/error.html
    Get Title    ==    Error Page

Template Error Page Is Visible When Using Incorrect Credentials
    [Arguments]    ${username}    ${password}
    Enter Username    ${username}
    Enter Password    ${password}
    Submit Login Form
    Verify That Error Page Is Visible
```

Now we've prepared our suite to get ready for data driven tests. Let's add the final piece to the `Settings` table.
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#data-driven-style

Add `Test Template` to the `Settings` table. Value for this setting should be
`Template Error Page Is Visible When Using Incorrect Credentials`.

We can then remove all of our existing test cases from `invalid_login.robot` test suite.

Our `Settings` table should look like this:

```robot
*** Settings ***
Library    Browser
Resource    resource.robot
Test Setup    Open Browser To Login Page
Test Template    Template Error Page Is Visible When Using Incorrect Credentials
```

Let's create our very first data driven test case.

So now that we're using the data driven style of creating test case, under test case table we can write
`<name_of_the_test_case>    <username>    <password>`. Like this:

```robot
*** Test Cases ***
#test case name                  #username   #password
Empty Username Empty Password    ${EMPTY}    ${EMPTY}
```

Now run `robot robot/invalid_login.robot` command to verify that changes are done correctly.

Now let's create 4 more test cases. Just add new line `<name of the test case> 4 spaces <username> 4 spaces <password>`
and voilà. We've now a new test case.

Once you've implemented all 5 test cases run:

- Windows: double-click the `07-test_template.cmd`
- Linux/macOS: run `./exercises/verify/07-test_template.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
