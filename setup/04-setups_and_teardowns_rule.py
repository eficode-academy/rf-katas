from rflint.common import TestRule, ERROR
from static import normalize

SUCCESSFUL_LOGIN = "Do Successful Login"
SUCCESSFUL_LOGOUT = "Do Successful Logout"

class TestSettingsCheck(TestRule):
    severity = ERROR

    def apply(self, test):
        report = True
        settings = []
        expected_settings = []
        for setting in test.settings:
            settings.append(normalize(setting[2]))
        if normalize(test.name) == "Welcome Page Should Be Visible After Successful Login":
            expected_settings.append(SUCCESSFUL_LOGOUT)
            if SUCCESSFUL_LOGOUT in settings:
                report = False
        elif normalize(test.name) == "Login Form Should Be Visible After Successful Logout":
            expected_settings.append([SUCCESSFUL_LOGIN])
            if SUCCESSFUL_LOGIN in settings:
                report = False
        if report:
            self.report(test, f"Check out that you've added needed setup and/or teardown for your test: {test.name}, expected: {', '.join(expected_settings)}", test.linenumber)
