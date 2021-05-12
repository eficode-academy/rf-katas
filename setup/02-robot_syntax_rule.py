from rflint.common import SuiteRule, TestRule, ERROR, WARNING
from static import normalize

MUST_KEYWORDS = [
        "Open Browser",
        "Input Text",
        "Input Password"
    ]

LOGIN_KEYWORDS = [
        "Click Element",
        "Click Button",
        "Submit Form"
]

VERIFY_KEYWORDS = [
        "Page Should Contain",
        "Page Should Contain Element",
        "Title Should Be",
        "Wait Until Page Contains",
        "Wait Until Page Contains Element"
]

class TestCaseImplementation02(TestRule):
    severity = ERROR

    def normalize(self, kw):
        return kw.strip().title()

    def apply(self, test):
        default_message = "Did you find all keywords from SeleniumLibrary documentation?"
        report = False
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(normalize(step[1]))

        for keyword in MUST_KEYWORDS:
            if not normalize(keyword) in test_steps:
                report = True
        if report:
            self.report(test, default_message + ", expected: {}".format(", ".join(MUST_KEYWORDS)), test.linenumber)

        for keyword in test_steps:
            if normalize(keyword) in LOGIN_KEYWORDS:
                break
        else:
            self.report(test, default_message + ", expected one of: {}".format(", ".join(LOGIN_KEYWORDS)), test.linenumber)

        for keyword in test_steps:
            if normalize(keyword) in VERIFY_KEYWORDS:
                break
        else:
            self.report(test, default_message + ", expected one of: {}".format(", ".join(VERIFY_KEYWORDS)), test.linenumber)

class TestCaseKeywordCases02(TestRule):
    severity = WARNING

    def apply(self, test):
        default_message = "Did you find all keywords from seleniumlibrary documentation?"
        report = False
        for step in test.steps:
            if len(step) > 1:
                if step[1] != normalize(step[1]):
                    self.report(test, "Best practice is to Capitalize All The Words In A Keyword: " + step[1] , test.linenumber)


class CheckTestCasesName02(SuiteRule):

    severity = ERROR

    def apply(self, suite):
        expected_name = "Welcome Page Should Be Visible After Successful Login"
        for testcase in suite.testcases:
            if testcase.name.lower() != expected_name.lower():
                self.report(suite, "Check test case name: {}, expected: {}".format(testcase.name, expected_name), 0)
