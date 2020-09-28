from rflint.common import KeywordRule, SuiteRule, TestRule, ERROR

ALLOWED_KEYWORDS = [
    "Open Browser To Login Page",
    "Enter Username",
    "Enter Password",
    "Submit Login Form",
    "Verify That Error Page Is Visible"
]


class KeywordImplementationRule05(KeywordRule):
    severity = ERROR

    def apply(self, keyword):
        report = False
        if keyword.name == ALLOWED_KEYWORDS[1] or keyword.name == ALLOWED_KEYWORDS[2]:
            if len(keyword.settings) == 0 or (not "[Arguments]" in keyword.settings[0]):
                report = True
        if report:
            self.report(keyword, "Did you remember to use keyword arguments?", keyword.linenumber)

class TestCaseImplementation05(TestRule):
    severity = ERROR

    def apply(self, test):
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(step[1])
        if test_steps != ALLOWED_KEYWORDS:
            self.report(test, "Check that you've implemented test case {} as instructed, expected: {}".format(test.name, ", ".join(ALLOWED_KEYWORDS)), test.linenumber)