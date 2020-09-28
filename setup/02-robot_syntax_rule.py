from rflint.common import SuiteRule, TestRule, ERROR

MUST_KEYWORDS = [
        "Open Browser",
        "Input Text",
        "Page Should Contain"
    ]

class TestCaseImplementation02(TestRule):
    severity = ERROR

    def apply(self, test):
        report = False
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(step[1])
        for keyword in MUST_KEYWORDS:
            if not keyword.strip() in test_steps:
                report = True
        if report:
            self.report(test, "Did you find all keywords from seleniumlibrary documentation?, expected: {}".format(", ".join(MUST_KEYWORDS)), test.linenumber)

class CheckTestCasesName02(SuiteRule):

    severity = ERROR

    def apply(self, suite):
        expected_name = "Welcome Page Should Be Visible After Successful Login"
        for testcase in suite.testcases:
            if testcase.name.lower() != expected_name.lower():
                self.report(suite, "Check test case name: {}, expected: {}".format(testcase.name, expected_name), 0)
