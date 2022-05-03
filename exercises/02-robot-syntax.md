# Robot Syntax

<details>
    <summary>In the previous exercise we created <code>robot/login.robot</code> file and the content was most likely something like this</summary>

```text
Open browser
Navigate to localhost:7272
Enter username
Enter password
Submit login form
Check that welcome page text is visible
```

</details>

If you now run command `robot robot/login.robot` you should get something like this:

`[ ERROR ] Parsing 'robot/login.robot' failed: File has no tests or tasks.`

or

`[ ERROR ] Suite 'Login' contains no tests or tasks.`

The reason is that this is not in Robot syntax.

Check out Robot Framework user guide: [Creating test data](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-data).

## Terminology

Robot files are split into parts and those parts are called tables.
Each table starts with `***` and ends with `***`.

There are 5 types of tables:

- `*** Settings ***` - to define libraries, resources, suite/test setups, documentation, etc:
[See all available settings](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#all-available-settings-in-test-data).
- `*** Variables ***` - to define suite level variables:
[See different variables](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variable-section).
- `*** Keywords ***` - user defined keywords:
[See creating keywords](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords).
- `*** Test Cases ***` - All the suite (file) test cases goes below this one:
[See test case syntax](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-case-syntax).
- `*** Tasks ***` - Alternative to test cases, used in Robotic Process Automation (RPA):
[See creating tasks](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-tasks).

For more details, check the Robot Framework user guide about
[test data syntax](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-data-syntax).

## Exercise

In order to fix the Robot output from `robot/login.robot`, let's add the missing test case table
`*** Test Cases ***` to define we have test cases in the file. This tells Robot that the file contains a **test suite**.

- Add a test case table to your test suite.

Once you've added the test case table let's run the command `robot robot/login.robot`

Using the snippet from earlier we should get output:

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
belongs. Each indented line is called a **keyword**.

In order to make Robot understand that want to have 1 test case with 6 steps we need to define it like this:

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    Open browser
    ...
```

If we take a closer look at the Browser library documentation, we notice that there isn't
a keyword called `Open browser`. However, there is a keyword called
[`New Page`](https://marketsquare.github.io/robotframework-browser/Browser.html#New%20Page),
which does exactly what we want. Let's change our `Open browser` to that.

- Define a test case called `Welcome Page Should Be Visible After Successful Login`.
- Indent all the manual steps you had written by 4 spaces, so that they are part of your test case.
- Replace your `Open browser` step to be `New Page`.

Note that keywords are actually case-insensitive, so `new page`, `NEW PAGE`, `New page`,
and `NeW pAgE` will all work. However, the recommended way is to capitalize the first letter of
each word, like `New Page` in this case. More information can be found from the
*[How to write good test cases using Robot Framework](https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst#naming)*-guide.

After that run `robot robot/login.robot` and the output should be something like this:

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

This is because Robot Framework has built-in libraries that come along when you run `pip install robotframework` and
will work "out of the box" without you having to worry about anything. However, most of the needed libraries (such as
the Browser) are external and provided by the open source community. We need to tell Robot separately
to use them.

See the user guide for
[importing libraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#importing-libraries).

So, in order to take Browser into use during runtime we need to add a `*** Settings ***` table and add
the library definition there.

After `Library` you need to have _at least_ 2 spaces (preferably 4) before defining the library name:
`Library    SomeLibrary`.

- Add a settings table at the beginning of your test suite.
- Add a library import to import `Browser`.

Once you've added the `Settings` table and told Robot to use Browser you can run `robot robot/login.robot`
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

As the test starts, the `No keyword with name 'New Page' found.` error does not pop up anymore. This
means that opening a new page now works - or does it? Nothing seems to open. This is because the browser
opens by default in a _headless_ state. Headless simply means that the GUI is not visible and the idea
is to make test performance better. We need to open the browser specifically in a headful state if we
want to see what is happening during the test.

Before getting into how to do that, let's explain three important Browser-library concepts: browser,
context, and page.

1. _Browser_ indicates a browser - Chromium (Chrome, Edge, Opera), Firefox, or WebKit (Safari).
2. _Context_ includes cookies, sessions, profile settings etc. A context is opened within a browser.
3. _Page_ is simply a webpage (or a tab) which is opened inside a browser. A page is opened within a context.

So when we call the `New Page` keyword without any context or browser created, what the keyword actually
does is that it calls `New Browser` and `New Context` first. These calls are done with default settings.
As it happens, a browser opens headless by default.

We don't need to touch the context, so we will let run with default values. However,
we want to open a browser in a headful state, we'll have to call the `New Browser` separately
(before calling `New Page`) with a specific argument defining this: `headless=${FALSE}`. This is called a
keyword **argument**. Keyword arguments are added to the same line as the keyword each argument separated by
(preferably) 4 spaces. For example, imagine we have a keyword called `Add` which takes two arguments `arg1` and `arg2`,
we can call it by using either of the following:

```robot
Add    1    2
Add    arg1=1    arg2=2
```

- Add a `New Browser` call before `New Page`
- Add 4 spaces and `headless=${FALSE}` after `New Browser` (on the same line).

Running the tests headful is not necessary for the final test, but it makes debugging a lot easier
as we then see what the tests are doing.

So now the test case should look like something like below.

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    New Browser    headless=${FALSE}
    New Page
    ...
```

Now, after running the test yet again, a browser will open, but it won't show any page. This is because
the `New Page` keyword was called without arguments. We need to add the necessary `url` arguments for `New Page` keyword.
Since the `url` is the first (and only) argument for `New Page` we can use it without specifying `url=some url`, unlike
when we had to use `headless=` for `New Browser`.

- Add 4 spaces and the URL to our website after the `New Page` keyword (on the same line).

Our `robot/login.robot` file look now something like this (note that all words were capitalized as recommended):

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

*Note:* Make sure that the SUT is running in its own window and that you can access it with address
http://localhost:7272.

Now you can see browser actually opening and accessing to SUT and then failing due to another keyword
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

After you've made the test pass, ensure that it's done with right manner by running:

- in Windows: run command `python verify.py 02`
- in macOS/Linux: run command `python3 verify.py 02`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
