from rflint.common import KeywordRule, SuiteRule, TestRule, ERROR

CLOSE_BROWSER = "Close Browser"

class TestSettingsCheck(TestRule):
    severity = ERROR

    def apply(self, test):
        report = True
        settings = []
        expected_settings = [CLOSE_BROWSER]
        for setting in test.settings:
                settings.append(setting[2])
        if test.name.strip() == "Welcome Page Should Be Visible After Successful Login":
            if CLOSE_BROWSER in settings:
                report = False
        elif test.name == "Login Form Should Be Visible After Successful Logout":
            expected_settings.append("Do Successful Login")
            if "Do Successful Login" in settings and CLOSE_BROWSER in settings:
                report = False
        if report:
            self.report(test, "Check out that you've added needed setup and/or teardown for your test: {}, expected: {}".format(test.name, ", ".join(expected_settings)), test.linenumber)
