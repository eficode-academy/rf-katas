# Robot Syntax
In the previous exercise, you wrote some manual instructions in a <code>robot/login.robot</code> file.

<details><summary>Our Solution</summary>

```text
Open browser
Navigate to localhost:7272
Enter username
Enter password
Submit login form
Check that welcome page text is visible
```

</details>


If you now run the command `robot robot/login.robot`, you should get something like this:

`[ ERROR ] Parsing 'robot/login.robot' failed: File has no tests or tasks.`

or

`[ ERROR ] Suite 'Login' contains no tests or tasks.`

The reason is that your steps don't follow Robot Framework syntax—yet.

> We'll cover the main parts of Robot Framework syntax in this guide, but if you ever get stuck, check the ["Test Data" syntax](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-data-syntax) section of the the Robot Framework User Guide.

## Terminology

Robot files are split into parts and those parts are called tables.
Each table header starts and ends with `***`.

There are 5 types of tables:

- `*** Settings ***` — to define libraries, resources, suite/test setups, documentation, etc:
[See all available settings](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#all-available-settings-in-test-data).
- `*** Variables ***` — to define suite level variables:
[See different variables](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variable-section).
- `*** Keywords ***` — user-defined keywords:
[See creating keywords](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords).
- `*** Test Cases ***` — groups of steps (a group = a test case):
[See test case syntax](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-case-syntax).
- `*** Tasks ***` — alternative name for test cases table; used in Robotic Process Automation (RPA):
[See creating tasks](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-tasks).

For more details, check the Robot Framework user guide about
[test data syntax](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-data-syntax).

## Exercise

Let's add the missing `*** Test Cases ***` table header and see how far that gets us. This tells the Robot Framework that the file contains a **test suite**.

- Add a test case table header to the top of your `login.robot` file.

Once you've added the test case table, let's run the command `robot robot/login.robot`

## Explanation

Your output should look something like this:

```text
==============================================================================
Login
==============================================================================
Open browser                                                          | FAIL |
Test case contains no keywords.
------------------------------------------------------------------------------
Navigate to localhost:7272                                            | FAIL |
Test case contains no keywords.
------------------------------------------------------------------------------
Enter username                                                        | FAIL |
Test case contains no keywords.
------------------------------------------------------------------------------
Enter password                                                        | FAIL |
Test case contains no keywords.
------------------------------------------------------------------------------
Submit login form                                                     | FAIL |
Test case contains no keywords.
------------------------------------------------------------------------------
Check that welcome page text is visible                               | FAIL |
Test case contains no keywords.
------------------------------------------------------------------------------
Login                                                                 | FAIL |
6 critical tests, 0 passed, 6 failed
6 tests total, 0 passed, 6 failed
```

The reason Robot thinks we have 6 test cases is because each unindented line in the `Test Cases` table is
considered as a new test case. When a line is indented by 4 spaces, it indicates to Robot that this
line belongs to the previous unindented line, be it test case, task, or keyword depending on the table it
belongs to. Each indented line is called a **keyword**.

In order to make Robot understand that you want to have 1 test case with 6 steps, we need to define it like this:

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login # <-Test Case
    Open browser # <-Step
    Navigate to localhost:7272 # <-Step
    # ... and so on
```

## Exercise

If we take a closer look at the [Browser library documentation](https://marketsquare.github.io/robotframework-browser/Browser.html), we notice that there isn't
a keyword called `Open browser`. However, there is a keyword called
[`New Page`](https://marketsquare.github.io/robotframework-browser/Browser.html#New%20Page),
which does exactly what we want. Let's change our `Open browser` to that.

- Define a test case called `Welcome Page Should Be Visible After Successful Login`.
- Indent all the manual steps you had written by 4 spaces, so that they are part of your test case.
- Replace `Open browser` with Browser's `New Page` keyword.

> Note that keywords are actually case-insensitive, so `new page`, `NEW PAGE`, `New page`,
and `NeW pAgE` will all work. However, the recommended way is to capitalize the first letter of
each word, like `New Page` in this case. More good habits can be found in the
*[How to write good test cases using Robot Framework](https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst#naming)*-guide.

After that, run `robot robot/login.robot` and the output should be something like this:

```text
==============================================================================
Login
==============================================================================
Welcome Page Should Be Visible After Successful Login                 | FAIL |
No keyword with name 'New Page' found.
------------------------------------------------------------------------------
Login                                                                 | FAIL |
1 critical test, 0 passed, 1 failed
1 test total, 0 passed, 1 failed
==============================================================================
```

### Test Libraries

Wait a minute... We just checked that `New Page` is a keyword in the Browser library. So _why_ doesn't
it show up?

This is because Browser isn't one of the _built-in_ libraries; lots of useful libraries are external and 
provided by the open source community. We need to tell Robot separately to use them.

> For more on [importing libraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#importing-libraries), see the user guide.

- "Enable" the Browser library, by adding a `*** Settings ***` table and including it there.

```robot
*** Settings ***
Library    Browser
```

 > After `Library` you need to have _at least_ 2 spaces (preferably 4) before defining the library name.

Once you've added the `Settings` table and told Robot to use Browser, you can run `robot robot/login.robot`
again and your output should be something like this:

```text
==============================================================================
Login
==============================================================================
Welcome Page Should Be Visible After Successful Login                 | FAIL |
No keyword with name 'Navigate to localhost:7272' found.
------------------------------------------------------------------------------
Login                                                                 | FAIL |
1 critical test, 0 passed, 1 failed
1 test total, 0 passed, 1 failed
==============================================================================
```

### Success?

As the test starts, the `No keyword with name 'New Page' found.` error does not pop up anymore. This
means that opening a new page now works — or does it? Nothing seems to open. This is because the browser
opens by default in a _headless_ state. Headless simply means that the GUI is not visible and the idea
is to make test performance better. We need to open the browser specifically in a headful state if we
want to see what is happening during the test.

## Browser-library Concepts
Before getting into how to do that, let's explain three important Browser-library concepts: browser,
context, and page.

1. _Browser_ indicates a browser — Chromium (Chrome, Edge, Opera), Firefox, or WebKit (Safari).
2. _Context_ includes cookies, sessions, profile settings etc. A context is opened within a browser.
3. _Page_ is simply a webpage (or a tab) which is opened inside a browser. A page is opened within a context.

So when we call the `New Page` keyword without any context or browser created, what the keyword actually
does is that it calls `New Browser` and `New Context` first. These calls are done with default settings.
As it happens, a browser opens headless by default.

### Getting a "headful" browser
We don't need to touch the context, so we will let it run with default values. However,
we want to open a browser in a headful state, we'll have to call the `New Browser` separately
(before calling `New Page`) with a specific argument defining this: `headless=${FALSE}`. This is called a
keyword _argument_. Keyword arguments are added to the same line as the keyword; each argument is separated by
(preferably) 4 spaces. 

For example, imagine we have a keyword called `Add` which takes two arguments `arg1` and `arg2`, we can call it 
by using either of the following:

```robot
Add    1    2
Add    arg1=1    arg2=2
```

- Add a `New Browser` call before `New Page`
- Add 4 spaces and `headless=${FALSE}` after `New Browser` (on the same line).

Running the tests headfully is not necessary for the final test, but it makes debugging a lot easier
as we then see what the tests are doing.

So now the test case should look like something like below.

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    New Browser    headless=${FALSE}
    New Page
    # ...
```

Now, after running the test yet again, a browser will open, but it won't show any page. This is because
the `New Page` keyword was called without arguments. We need to add the necessary `url` arguments for the `New Page` keyword.
Since the `url` is the first (and only) argument for `New Page` we can use it without specifying `url=some url`, unlike
when we had to use `headless=` for `New Browser`.

- Add 4 spaces and the URL to our website after the `New Page` keyword (on the same line).

Our `robot/login.robot` file now looks something like this (note that all words are capitalized as recommended):

```robot
*** Settings ***
Library    Browser

*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    New Browser    headless=${FALSE}
    New Page    http://localhost:7272
    Navigate To localhost:7272
    Enter Username
    Enter Password
    Submit Login Form
    Check That Welcome Page Text Is Visible
```

> *Note:* Make sure that the SUT is running in its own terminal window and that you can manually access it by navigating to http://localhost:7272. If it's not running, start the server by running `python3 server/server.py`

Now you can see the browser actually opening and  accessing the SUT but then failing due to another keyword
not found exception.

- If you have something like `Navigate to localhost:7272`, remove it since the `New Page` will
already go to that website.

- Find 3 appropriate keywords from the
[keyword documentation](https://marketsquare.github.io/robotframework-browser/Browser.html)
to fill the username and password and click the login button.

In order to find a value for the `selector` argument of your selected keywords, you need to open
the source code for the web page to find the element IDs. You can do that by right-clicking anywhere in the page
and choosing `Inspect`.

To verify that welcome page is visible you can check the page content, URL and/or title. With the Browser-library,
verifications (or assertions) can be done in combination with the `Get ...`-keywords,
For example all the following assertions verify that the `title` is `Welcome Page`:

```robot
Get Title    ==    Welcome Page
Get Title    Equals    Welcome Page
Get Title    Should Be    Welcome Page
```

See more information from supported [assertions](https://marketsquare.github.io/robotframework-browser/Browser.html#Assertions).

- Add an assertion for your test case to verify your test lands on the welcome page.

After you've successfully run the test case with `robot robot/login.robot` you should see output like this:

```text
==============================================================================
Login
==============================================================================
Welcome Page Should Be Visible After Successful Login                 | PASS |
------------------------------------------------------------------------------
Login                                                                 | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
```

### Verification

After you've made the test pass, ensure that it's done in the right manner by running:

- Windows: double click `02-robot_syntax.cmd`
- Linux/macOS: run `./exercises/verify/02-robot_syntax.sh`

If you see "Ready to proceed!", then you're done for the exercise. Otherwise, check the output, fix your file, and re-run the verification.