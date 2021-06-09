# Keywords and variables

One of the most powerful things that Robot Framework can do is to provide capability to write test cases
with natural language. In an ideal world other people are also interested on the automated test case results and
how, where, and when they are run.

This can be achieved by using user defined keywords:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords

## User defined keywords

With user defined keywords we can create abstraction layer when needed.
A general rule of thumb is that library and resource keywords are "general sounding" ones and with user keywords in test suite you can create needed abstraction layer based on the test context.

<details>
    <summary>From previous exercises we should have something like this in our <code>robot/login.robot</code></summary>

```
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    Open Browser    http://localhost:7272   browser=ff
    Input Text    id=username_field    demo
    Input Password    id=password_field    mode
    Click Element    id=login_button
    Page Should Contain    Welcome Page
    Location Should Be    http://localhost:7272/welcome.html
    Title Should Be    Welcome Page
```

</details>

This test is technically correct, but can be quite hard to read if you don't know e.g. what is HTML attribute `id`.

In other words, we need to refactor our test a bit.

We need to add a new table `*** Keywords ***`. It can be above or below the `*** Test Cases ***`.

Under `Keywords` table we need to create a new keyword called `Open Browser To Login Page`. The same indentation
rules apply with keywords as in test cases: each unindented line is considered a new keyword, so the implementation
of the keyword need to be indented with 4 spaces.

```
*** Keywords ***

Open Browser To Login Page
    Open Browser    http://localhost:7272   browser=ff
```

Now, we can replace our `Open Browser    http://localhost:7272   browser=ff` from our test case with our own
user defined keyword `Open Browser To Login Page` to provide context to our test case.

You can test out that your refactoring was done correctly by running `robot robot/login.robot` and to see that test is still passing.

After the possible fixes create the following keywords:

  - `Enter Username`
  - `Enter Password`
  - `Submit Login Form`
  - `Verify That Welcome Page Is Visible`

*Pro tip 1* A user defined keyword can run multiple keywords, just like a test case can have multiple steps.

*Pro tip 2* Check out also arguments for user keywords: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#user-keyword-arguments

After you've defined and implemented the keywords your test case should look like this:

```
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    Open Browser To Login Page
    Enter Username    demo
    Enter Password    mode
    Submit Login Form
    Verify That Welcome Page Is Visible
```

Ensure you refactored test is still passing by running `robot robot/login.robot`.

But hey! Doesn't our test case look nice and clean? With UTF-8 support you can write those user defined keywords and test case names practically any language that you want: Finnish, Swedish, Russian, Traditional Chinese, what ever suites your project/company policy.


## Variables

Robot Framework does support variables: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variables

A benefit of using variables instead of hard coded values is to provide a single place where to change the value and then tests are working once again if nothing else has changed. This will increase the maintainability of the test cases.

Let's modify our test to use variables.

A key aspect in using variables is discovering what values could change more often. For example, one that is likely
to change is the location where the SUT is running. In order to add variables to our test suite,
we need to create a `*** Variables ***` table.

Defining variables can be done with the following syntax:
```
${VARIABLE_NAME}=    variable value
```

The `=` is optional and can be removed if you don't want to use it. You still need to have at least 2 spaces
(preferably at least 4) between `${VARIABLE_NAME}` and `variable value`. Also, variable names are completely
case-insensitive, but the best practice is to define variables in the `Variables` table in ALL CAPS. This is
purely to better distinguish the scope of variables (full caps for global, suite, and test variables and small
case for keyword variables).

Let's add our `Variables` table and `URL` as a variable.

```
*** Variables ***
${URL}=    http://localhost:7272
```

Now replace all the existing `http://localhost:7272` with `${URL}`.

*Pro tip* You can combine variables with text like this `${URL}/` or `${URL}/welcome.html` without any concatenation or aritmethic operations.

After you've made changes, run the `robot robot/login.robot` to verify that the test is still passing.

*Pro tip* If you don't want to actually run the test case but just check the syntax you can also run `robot --dryrun robot/login.robot`. Check `robot -h` for more details.


Now that you've successfully changed to use `${URL}` variable,
think about what other values could change except the domain of the SUT.
Create those variables and modify the test case to use them instead of hard coded values.

Once you've done those, run the `robot robot/login.robot` to verify that changes are done correctly.

To ensure that changes are done in right manner run:

  - Windows: double click the `03-keywords_and_variables.cmd`
  - Linux/macOS: run `./exercises/verify/03-keywords_and_variables.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise check the output and fix, rerun.
