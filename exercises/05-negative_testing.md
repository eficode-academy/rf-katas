# Negative testing

So far we have tested only "happy cases", which are test cases that prove the feature is working as
intended: when the user knows what they should do.

Let's focus on negative testing, which means testing that the application behaves correctly
when the user makes an error. In this case it means that the user inputs incorrect credentials.

## Exercise

Think about different ways to mistype a combination of username and password, and write them in some
file. Have at least 6 different combinations of incorrect credentials.

Checkout also Robot Framework [built-in variables](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables).

- Create a new file `invalid_login.robot` under `robot` folder.
- Write different combinations how to test invalid credentials.
    - You can write them to your new test suite file as comments. Commented lines start with `#` and are ignored when running Robot Framework.

After you've finished your list let's start implementing one of those.

- Create a test case `Error Page Should Be Visible After Incorrect Login` into the `invalid_login.robot`.
- Copy-paste the `Open Browser To Login Page`, `Enter Username`, `Enter Password`, and `Submit Login Form`
keywords from `login.robot` into `invalid_login.robot`. Normally we would not copy-paste keywords around;
we will see later on how to achieve this while keeping ourselves [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
- Create a keyword called `Verify That Error Page Is Visible` to check we've landed on the error page.

Run the test with `robot robot/invalid_login.robot` command to verify the results.

In this exercise the task is to only test one of the six combinations you thought of earlier. However,
there are at least six possible combinations. Creating a new keyword for entering credentials in each
and every of those cases is kind of unnecessary repetition, since the only changing part is the value
being entered in the field.

This is where keyword arguments should be used. Keyword arguments work
just like your variables in the `*** Variables ***` table, except it is best practice keyword arguments
to write them in lower case. Keyword arguments are defined in a similar fashion as setup and teardown in [exercise 04](./04-setups_and_teardowns.md)
by using `[Arguments]` on a new line after a keyword name.

- Define keyword arguments to `Enter Username` and `Enter Password` by putting `[Arguments]` after the
keyword name.
    - Add 4 spaces and a **variable** after `[Arguments]`.
- Replace the hard-coded value with your new argument.

<details>
    <summary>After these steps, you need four spaces and the name of your argument, resulting in:</summary>

```robot
Enter Username
    [Arguments]    ${username}
    Fill Text    id=username_field    ${username}
```

</details>

Note that if you have a `${USERNAME}` variable in the `*** Variables ***` table, and also use
`${username}` as a keyword argument, then inside that keyword all uses of both `${username}` and
`${USERNAME}` will access only that keyword argument variable (in programming, this is called
shadowing).

*Pro-tip:* The `Fill Secret` keyword might fail with an error saying `Invalid variable name ''`. This
originates from how that specific keyword handles variables. The filled data is considered as a _secret_, so the
idea would be not to log it, even to the log-file. More information can be found from the
[keyword-documentation](https://marketsquare.github.io/robotframework-browser/Browser.html#Fill%20Secret),
but generally the error can be fixed by replacing the variable reference `${password}` with `$password`,
as explained in the documentation.

## Verification

When the test passes run the following command to ensure that changes are done in right manner run:

- in Windows: run command `python verify.py 05`
- in macOS/Linux: run command `python3 verify.py 05`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise, check the output and fix, rerun.
