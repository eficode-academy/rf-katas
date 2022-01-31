from rflint.common import SuiteRule, TestRule, ERROR, WARNING
from static import normalize

MUST_KEYWORDS = [
    "New Browser",
    "New Page",
    "Fill Text",
    "Fill Secret",
]

LOGIN_KEYWORDS = [
    "Click",
    "Keyboard Key",
]

VERIFY_KEYWORDS = [
    "Get Title",
    "Get Url",
    "Get Text",
]

DEFAULT_MESSAGE = "Did you find all keywords from the Browser-library documentation?"

class TestCaseImplementation02(TestRule):
    severity = ERROR

    def apply(self, test):
        report = False
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(normalize(step[1]))

        for keyword in MUST_KEYWORDS:
            if not normalize(keyword) in test_steps:
                report = True
        if report:
            self.report(test, f"{DEFAULT_MESSAGE}, expected: {', '.join(MUST_KEYWORDS)}", test.linenumber)

        for keyword in test_steps:
            if normalize(keyword) in LOGIN_KEYWORDS:
                break
        else:
            self.report(test, f"{DEFAULT_MESSAGE}, expected one of: {', '.join(LOGIN_KEYWORDS)}", test.linenumber)

        for keyword in test_steps:
            if normalize(keyword) in VERIFY_KEYWORDS:
                break
        else:
            self.report(test, f"{DEFAULT_MESSAGE}, expected one of: {', '.join(VERIFY_KEYWORDS)}", test.linenumber)

class TestCaseKeywordCases02(TestRule):
    severity = WARNING

    def apply(self, test):
        report = False
        for step in test.steps:
            if len(step) > 1:
                if step[1] != normalize(step[1]):
                    self.report(test, f"Best practice is to Capitalize All The Words In A Keyword: {step[1]}", test.linenumber)


class CheckTestCasesName02(SuiteRule):
    severity = ERROR

    def apply(self, suite):
        expected_name = "Welcome Page Should Be Visible After Successful Login"
        for testcase in suite.testcases:
            if normalize(testcase.name) != expected_name:
                self.report(suite, f"Check test case name: {testcase.name}, expected: {expected_name}", 0)
