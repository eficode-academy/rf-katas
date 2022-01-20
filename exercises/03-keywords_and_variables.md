# Keywords and variables

One of the most powerful things that Robot Framework can do is to provide the capability to write test
cases using natural language. In an ideal world, it is not just people who write those tests, but also
other people are interested in the automated test case results, including how, where, and when they are
run.

This can be made possible by using user defined keywords:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords

## User defined keywords

With user defined keywords we can create abstraction layer when needed. A general rule of thumb is that
library and resource keywords are "general sounding" ones and with user keywords in test suite you can
create needed abstraction layer based on the test context.

<details>
    <summary>From previous exercises we should have something like this in our <code>robot/login.robot</code></summary>

```robot
*** Settings ***
Library    Browser

*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    New Browser    headless=${FALSE}
    New Page    http://localhost:7272
    Fill Text    id=username_field    demo
    Fill Secret    id=password_field    mode
    Click    id=login_button
    Get Text    body    contains    Welcome Page
    Get Url    ==    http://localhost:7272/welcome.html
    Get Title    ==    Welcome Page
```

</details>

This test is technically correct, but can be quite hard to read if you don't know e.g. what is an HTML
attribute `id`.

In other words, we need to refactor our test a bit.

We need to add a new table `*** Keywords ***`. It can be above or below the `*** Test Cases ***`.

Under the `Keywords` table we need to create a new keyword called `Open Browser To Login Page`. The
same indentation rules apply with keywords as in test cases: each unindented line is considered a new
keyword, so the implementation of the keyword need to be indented with 4 spaces.

```robot
*** Keywords ***

Open Browser To Login Page
    New Browser    headless=${FALSE}
    New Page    http://localhost:7272
```

Now, we can replace the first two lines from our test case with our own user defined keyword
`Open Browser To Login Page` to provide context to our test case.

You can test out that your refactoring was done correctly by running `robot robot/login.robot` and
to see that test is still passing.

After the possible fixes create the following keywords:

- `Enter Username`
- `Enter Password`
- `Submit Login Form`
- `Verify That Welcome Page Is Visible`

*Pro-tip 1:* One user defined keyword can contain multiple keywords, just like a test case can have
multiple steps. This can be used to shorten test cases by hiding long chains of actions inside aptly
named keywords.

*Pro-tip 2:* User defined keywords can become more versatile, through the use of arguments:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#user-keyword-arguments

After you've defined and implemented the keywords your test case should look like this:

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    Open Browser To Login Page
    Enter Username    demo
    Enter Password    mode
    Submit Login Form
    Verify That Welcome Page Is Visible
```

Ensure you refactored test is still passing by running `robot robot/login.robot`.

But hey! Doesn't our test case look nice and clean? With UTF-8 support you can write those user defined
keywords and test case names practically any language that you want: Finnish, Swedish, Russian, Traditional
Chinese, what ever suites your project/company policy.

## Variables

Robot Framework does support variables: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variables

A benefit of using variables instead of hard coded values here and there, is to provide a single place
where to change the value, when needed, which can return all the tests that use the variable back to
working once again (if nothing else needs changing). This will increase the maintainability of the test
cases.

Let's modify our test to use variables.

A key aspect in using variables is discovering what values could change more often. For example, one
that is likely to change is the location where the SUT is running. In order to add variables to our
test suite, we need to create a `*** Variables ***` table.

Defining variables can be done with the following syntax:

```robot
${VARIABLE_NAME} =    variable value
```

The `=` is optional and can be removed if you don't want to use it. You still need to have at least 2 spaces
(preferably at least 4) between `${VARIABLE_NAME}` and `variable value`. Also, variable names are completely
case-insensitive. Robot also ignores spaces and `_` signs. This means that to robot these variables names:
`${MYVARIABLE}`, `${MyVariable}`, `${MY VARIABLE}`, `${My_variable}`, and `${myvariable}` are actually all
referring to the same variable. The recommended best practice is to define variables in the `*** Variables ***`
table in ALL CAPS. This is purely to help everyone better distinguish the scope of variables (use upper
case for global, suite, and test variables and lower case for keyword variables).

Let's add our `Variables` table and `URL` as a variable.

```robot
*** Variables ***
${URL} =    http://localhost:7272
```

Now replace all the existing `http://localhost:7272` with `${URL}`.

*Pro-tip:* You can combine variables with text like this `${URL}/` or `${URL}/welcome.html` without
any concatenation or arithmetic operations.

After you've made changes, run the `robot robot/login.robot` to verify that the test is still passing.

*Pro-tip:* If you don't want to actually run the test case but just check the syntax you can also run
`robot --dryrun robot/login.robot`. Check `robot -h` for more details.

Now that you've successfully changed to use `${URL}` variable, think about what other values could
change except the domain of the SUT. Create those variables and modify the test case to use them instead
of hard coded values.

Once you've done those, run the `robot robot/login.robot` to verify that changes are done correctly.

To ensure that changes are done in right manner run:

- Windows: double-click the `03-keywords_and_variables.cmd`
- Linux/macOS: run `./exercises/verify/03-keywords_and_variables.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
