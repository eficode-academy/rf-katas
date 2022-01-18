# Robot Syntax

<details>
    <summary>In the previous exercise we created <code>robot/login.robot</code> file and the content was most likely something like this</summary>

```text
New page
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

Check out Robot Framework user guide: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-data

## Terminology

Robot files are split into parts and those parts are called tables.
Each table starts with `***` and ends with `***`.

There are 5 types of tables:

- `*** Settings ***` - to define libraries, resources, suite/test setups, documentation etc. http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#all-available-settings-in-test-data
- `*** Variables ***` - to define suite level variables http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variable-section
- `*** Keywords ***` - user defined keywords http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords
- `*** Test Cases ***` - All the suite (file) test cases goes below this one http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-case-syntax
- `*** Tasks ***` - http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-tasks

Check the Robot Framework syntax guide for more details: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-data-syntax

In order to fix the Robot output from `robot/login.robot`, let's add the missing test case table
`*** Test Cases ***` to define we have test cases in the file. This tells Robot that the file contains a test suite.

Once you've added the test case table let's run the command `robot robot/login.robot`

Using the snippet from earlier we should get output:

```text
==============================================================================
Login
==============================================================================
New page                                                              | FAIL |
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
considered as a new test case.

In order to make Robot understand that want to have 1 test case with 6 steps we need to define it like this:

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
```

Now in order to have the `New Page` we need to define it under the test case and in robot that is done with 4 spaces.

Note that keywords are actually case-insensitive, so `new page`, `NEW PAGE`, `New page`,
and `NeW pAgE` will all work. However, the recommended way is to capitalize the first letter of
each word, like `New Page` in this case. More information can be found from the
*[How to write good test cases using Robot Framework](https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst#naming)*-guide.

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    New Page
```

With 4 spaces at the beginning of the line indicates to robot that this keyword belongs to test case
or keyword depending on the table that was defined.

Now add all missing keywords as test step to our `Welcome Page Should Be Visible After Successful Login`

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

## Test Libraries

Robot now fails with `No keyword with name 'New Page' found.` but if we check the installed
Browser-library's documentation, we can see that there is in fact a keyword named `New Page`:
https://marketsquare.github.io/robotframework-browser/Browser.html#New%20Page. So _why_ doesn't
it show up?

This is because Robot Framework has built-in libraries that come along when you run `pip install robotframework` and
will work "out of the box" without you having to worry about anything. However, most of the needed libraries (such as
the Browser) are external and provided by the open source community. We need to tell Robot separately
to use them.

Check the library injection chapter from the user guide: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#importing-libraries

So, in order to take Browser into use during runtime we need to add a `*** Settings ***` table and add
the library definition there.

After `Library` you need to have _at least_ 2 spaces (preferably 4) before defining the library name:
`Library    SomeLibrary`.

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

Before getting into how to do that, let's expain three important Browser-library concepts: browser,
context, and page.

- _Browser_ indicates a browser - Chromium (Chrome, Edge, Opera), Firefox, or Webkit (Safari).
- _Context_ includes cookies, sessions, profile settings etc. A context is opened within a browser.
- _Page_ is simply a webpage (or a tab) which is opened inside a browser. A page is opened within a context.

So when we call the `New Page` keyword without any context or browser created, what the keyword actually
does is that it calls `New Browser` and `New Context` first. These calls are done with default settings.
As it happens, a browser opens headless by default.

If we want to open a browser in a headful state, we'll have to call the `New Browser` separately
(before calling `New Page`) with a specific argument defining this: `headless=${FALSE}`. The context
is still created with default arguments, and at this point there's no need to adjust those.

*Pro tip:* as everything else, arguments can be specified by leaving at least 2 (preferably 4) spaces
between the keyword and them.

Running the tests headful is not necessary for the final test, but it makes debugging a lot easier
as we then see what the tests are doing.

So now the test case should look like something like below.

```robot
*** Test Cases ***

Welcome Page Should Be Visible After Successful Login
    New Browser    headless=${FALSE}
    New Page
```

Now, after running the test yet again, a browser will open, but it won't show any page. This is because
the keyword was called without arguments.

So now we need to add the necessary arguments for `New Page` keyword: https://marketsquare.github.io/robotframework-browser/Browser.html#New%20Page.

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

*Note:* Make sure that the SUT is running on it's own windows and that you can access it with address
http://localhost:7272.

Now you can see browser actually opening and accessing to SUT and then failing due to another keyword
not found exception.

If you have something like `Navigate to localhost:7272` that can be removed since the `New Page` will
already go to that website.

Your job now is to figure out what Browser-library keywords you can use to input username and password,
and click the login element.

You need to open the source code for the web page to find the element IDs.

To verify that welcome page is visible you can check the page content, url and title. With the Browser-library,
vefications (or assertions) can be done in combination with the `Get ...`-keywords, for example `Get Title    ==    Welcome Page`. More information at https://marketsquare.github.io/robotframework-browser/Browser.html#Assertions.

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

After you've made the test pass, ensure that it's done with right manner by running:

- Windows: double click `02-robot_syntax.cmd`
- Linux/macOS: run `./exercises/verify/02-robot_syntax.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise check the output and fix, rerun.
