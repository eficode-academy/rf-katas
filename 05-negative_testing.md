# Negative testing

So far we have tested only "happy cases", which are test cases that proves that the feature is working as
intended, when the user knows what they should do.

Let's focus on negative testing, which means testing the application behaviour when the user makes an error.
In this case it means that the user types incorrect credentials.

Think about different ways to mistype username and password combinations and write them on some file. Have at least 6 different combinations of incorrect credentials.

Checkout also Robot Framework built-in variables: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables

After you've finished your list let's start testing one of those.

Create a new file `invalid_login.robot` under `robot` folder.

Create a test case `Error Page Should Be Visible After Incorrect Login` into the `invalid_login.robot`. Remember to create keyword `Verify That Error Page Is Visible`.

Run the test with `robot robot/invalid_login.robot` command to verify the results.

When the test passes run the following command to ensure that changes are done in right manner run:

  - Windows: double click the `05-negative_testing.cmd`
  - Linux/macOS: run `./05-negative_testing.sh`

If you see `Ready to proceed!` then you're done for the exercise. Otherwise check the output and fix, rerun.

