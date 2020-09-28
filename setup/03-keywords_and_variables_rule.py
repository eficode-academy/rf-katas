from rflint.common import KeywordRule, SuiteRule, TestRule, ERROR
from rflint.parser import SettingTable

ALLOWED_KEYWORDS = [
    "Open Browser To Login Page",
    "Enter Username",
    "Enter Password",
    "Submit Login Form",
    "Verify That Welcome Page Is Visible"
]

class InvalidKeywordName(KeywordRule):
    severity = ERROR

    def apply(self, keyword):
        if not keyword.name in ALLOWED_KEYWORDS:
            self.report(keyword, "Keyword {} not allowed in {}".format(keyword.name, ", ".join(ALLOWED_KEYWORDS)), keyword.linenumber)

class KeywordImplementation(KeywordRule):
    severity = ERROR

    def apply(self, keyword):
        report = False
        if keyword.name == ALLOWED_KEYWORDS[0]:
            if not "${URL}" in keyword.steps[0][2]:
                report = True
        if report:
            self.report(keyword, "Do you have URL variable in place? Check keyword: {}".format(ALLOWED_KEYWORDS[0]), keyword.linenumber+1)

class TestCaseImplementation(TestRule):
    severity = ERROR

    def apply(self, test):
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(step[1])
        if test_steps != ALLOWED_KEYWORDS:
            self.report(test, "Check that you've refactored test case {} in right manner, expected: {}".format(test.name, ", ".join(ALLOWED_KEYWORDS)), test.linenumber)