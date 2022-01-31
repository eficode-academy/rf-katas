from rflint.common import SuiteRule, ERROR

class NumberOfTestCases(SuiteRule):

    severity = ERROR
    max_test_cases = 1

    def configure(self, max_test_cases):
        self.max_test_cases = int(max_test_cases)

    def apply(self, suite):
        test_cases = []
        for testcase in suite.testcases:
            test_cases.append(testcase.name)
        if len(test_cases) != self.max_test_cases:
            self.report(suite, f"Check that you've implemented all test cases instructed in exercise, expected: {self.max_test_cases}", 0)

class NumberOfKeywordsInTestSuite(SuiteRule):
    severity = ERROR
    max_keywords = 1
    keyword_names = []

    def configure(self, max_keywords):
        self.max_keywords = int(max_keywords)

    def apply(self, suite):
        for keyword in suite.keywords:
            self.keyword_names.append(keyword.name)
        if len(self.keyword_names) != self.max_keywords:
            self.report(suite, f"Check that you've implemented all keywords from exercise, expected: {self.max_keywords}", 0)