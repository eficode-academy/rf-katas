# Test templates

<details>
    <summary>After the previous exercise our <code>invalid_login.robot</code>
    should look something like this</summary>

```
*** Settings ***
Library    SeleniumLibrary
Resource    resource.robot

*** Variables ***

*** Test Cases ***

Error Page Should Be Visible After Invalid Login With Empty And Space
    Open Browser To Login Page
    Enter Username    ${EMPTY}
    Enter Password    ${SPACE*2}
    Submit Login Form
    Verify That Error Page Is Visible
    [Teardown]    Close Browser

Error Page Should Be Visible After Invalid Login With Valid Username And Invalid Password
    Open Browser To Login Page
    Enter Username    ${USERNAME}
    Enter Password    asdsadsa
    Submit Login Form
    Verify That Error Page Is Visible
    [Teardown]    Close Browser

Error Page Should Be Visible After Invalid Login With Invalid Username And Valid Password
    Open Browser To Login Page
    Enter Username    asdsadsa
    Enter Password    ${PASSWORD}
    Submit Login Form
    Verify That Error Page Is Visible
    [Teardown]    Close Browser

*** Keywords ***

Verify That Error Page Is Visible
    Page Should Contain    Error Page
    Location Should Be    ${URL}/error.html
    Title Should Be    Error Page
```

</details>

So, basically what most of us did was copy-pasted the first test several times, changed the test names
and changed the entered usernames and passwords. The tests do test different things and work well, but it
doesn't really make sense to copy-paste several lines and modify 2 parameters. Instead, we should use
test templates: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates

So far we've been doing so-called workflow tests. Test templates are so-called data driven tests, which are
usable when you need to run the same test multiple times and need to modify only a couple of arguments for
each test.

Let's get started. Rename the first test case `Template Error Page Is Visible When Using Incorrect Credentials`
and move it from the `Test Cases` table under the `Keywords` table.

Notice also that we have `[Teardown]` after every test separately. We can get rid of those by adding `Test Teardown`
into our `Settings` table. Our `Template Error Page Is Visible When Using Incorrect Credentials` keyword also
starts with `Open Browser to Login Page`, which is repeated in every test and it's not really part of the test. We
can add a `Test Setup` into our `Settings` table as well. After making those changes we can delete those lines
from `Error Page Is Visible When Using Incorrect Credentials`.

Also remember to add arguments for `Template Error Page Is Visible When Using Incorrect Credentials`.

*Pro tip.* A keyword can take multiple arguments when separating them with 4 spaces.

So now our `Settings` table should look like this:

```
*** Settings ***
Library    SeleniumLibrary
Resource    resource.robot
Test Setup    Open Browser To Login Page
Test Teardown    Close Browser
```

And `Keywords` table:

```
*** Keywords ***

Verify That Error Page Is Visible
    Page Should Contain    Error Page
    Location Should Be    ${URL}/error.html
    Title Should Be    Error Page

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

```
*** Settings ***
Library    SeleniumLibrary
Resource    resource.robot
Test Setup    Open Browser To Login Page
Test Teardown    Close Browser
Test Template    Template Error Page Is Visible When Using Incorrect Credentials
```

Let's create our very first data driven test case.

So now that we're using the data driven style of creating test case, under test case table we can write `<name_of_the_test_case> <username> <password>`. Like this:

```
*** Test Cases ***
#test case name                  #username   #password
Empty Username Empty Password    ${EMPTY}    ${EMPTY}
```

Now run `robot robot/invalid_login.robot` command to verify that changes are done correctly.

Now let's create 4 more test cases. Just add new line <name of the test case> 4 spaces <username> 4 spaces <password> and voilá. We've now a new test case.

Once you've implemented all 5 test cases run:

  - Windows: double click the `07-test_template.cmd`
  - Linux/macOS: run `./verify/07-test_template.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise check the output and fix, rerun.
