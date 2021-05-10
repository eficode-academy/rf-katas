from rflint.common import SuiteRule, TestRule, ERROR

MUST_KEYWORDS = [
        "Open Browser",
        "Input Text",
        "Input Password"
    ]

LOGIN_KEYWORDS = [
        "Click Element",
        "Click Button"
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

    def apply(self, test):
        default_message = "Did you find all keywords from seleniumlibrary documentation?"
        report = False
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(step[1].lower())
        for keyword in MUST_KEYWORDS:
            if not keyword.strip().lower() in test_steps:
                report = True
        if report:
            self.report(test, default_message + ", expected: {}".format(", ".join(MUST_KEYWORDS)), test.linenumber)
        report = False
        for keyword in test_steps:
            if keyword.title() in LOGIN_KEYWORDS:
                break
        else:
            report = True
        if report:
            self.report(test, default_message + ", expected one of: {}".format(", ".join(LOGIN_KEYWORDS)), test.linenumber)

        report = False
        for keyword in test_steps:
            if keyword.title() in VERIFY_KEYWORDS:
                break
        else:
            report = True
        if report:
            self.report(test, default_message + ", expected one of: {}".format(", ".join(VERIFY_KEYWORDS)), test.linenumber)

class CheckTestCasesName02(SuiteRule):

    severity = ERROR

    def apply(self, suite):
        expected_name = "Welcome Page Should Be Visible After Successful Login"
        for testcase in suite.testcases:
            if testcase.name.lower() != expected_name.lower():
                self.report(suite, "Check test case name: {}, expected: {}".format(testcase.name, expected_name), 0)
