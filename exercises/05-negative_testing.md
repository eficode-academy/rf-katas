# Negative testing

So far we have tested only "happy cases", which are test cases that prove the feature is working as
intended: when the user knows what they should do.

Let's focus on negative testing, which means testing that the application behaves correctly
when the user makes an error. In this case it means that the user inputs incorrect credentials.

Think about different ways to mistype a combination of username and password, and write them in some
file. Have at least 6 different combinations of incorrect credentials.

Checkout also Robot Framework built-in variables: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables

After you've finished your list let's start implementing one of those.

Create a new file `invalid_login.robot` under `robot` folder.

Create a test case `Error Page Should Be Visible After Incorrect Login` into the `invalid_login.robot`.
Copy-paste the `Open Browser To Login Page`, `Enter Username`, `Enter Password`, and `Submit Login Form`
keywords from `login.robot` into `invalid_login.robot`. Normally we would not copy-paste keywords around;
we will see later on how to achieve this while keeping ourselves [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
Remember to also create the keyword `Verify That Error Page Is Visible`.

Run the test with `robot robot/invalid_login.robot` command to verify the results.

In this exercise the task is to only test one of the six combinations you thought of earlier. However,
there are at least six possible combinations. Creating a new keyword for entering credentials in each
and every of those cases is kind of unnecessary repetition, since the only changing part is the value
being entered in the field. This is where keyword arguments should be used. Keyword arguments work
just like your variables in the `*** Variables ***` table, except it is best practice keyword arguments
to write them in lower case.

Define keyword arguments to `Enter Username` and `Enter Password` by putting `[Arguments]` after the
keyword name, just like you did with test `[Setup]` for a test case in [exercise 04](./04-setups_and_teardowns.md).
After these steps, you need four spaces and the name of your argument, resulting in:

```robot
Enter Username
    [Arguments]    ${username}
```

Also remember to change the input value in the `Fill Text` keyword to use the `${username}` variable
instead of a hard-coded value.

Note that if you have a `${USERNAME}` variable in the `*** Variables ***` table, and also use
`${username}` as a keyword argument, then inside that keyword all uses of both `${username}` and
`${USERNAME}` will access only that keyword argument variable (in programming, this is called
shadowing).

*Pro tip:* The `Fill Secret` keyword might fail with an error saying `Invalid variable name ''`. This
originates from how that specifc keyword handles variables. The filled data is considered as a _secret_, so the
idea would be not to log it, even to the log-file. More information can be found from the [keyword-documentation](https://marketsquare.github.io/robotframework-browser/Browser.html#Fill%20Secret),
but generally the error can be fixed by replacing the variable reference `${password}` with `$password`,
as explained in the documentation.

When the test passes run the following command to ensure that changes are done in right manner run:

- Windows: double click the `05-negative_testing.cmd`
- Linux/macOS: run `./exercises/verify/05-negative_testing.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise check the output and fix, rerun.
