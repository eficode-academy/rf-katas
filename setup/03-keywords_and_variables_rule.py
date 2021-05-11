from rflint.common import KeywordRule, SuiteRule, TestRule, GeneralRule, ERROR, WARNING
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
        if not keyword.name.title() in ALLOWED_KEYWORDS:
            self.report(keyword, "Keyword {} not allowed in {}".format(keyword.name, ", ".join(ALLOWED_KEYWORDS)), keyword.linenumber)

class KeywordImplementation(KeywordRule):
    severity = ERROR

    def apply(self, keyword):
        report = False
        if keyword.name.title() == ALLOWED_KEYWORDS[0]:
            if not "${URL}" in keyword.steps[0][2].upper():
                report = True
        if report:
            self.report(keyword, "Do you have URL variable in place? Check keyword: {}".format(ALLOWED_KEYWORDS[0]), keyword.linenumber+1)

class KeywordsShouldStartWithCapitalLetter(KeywordRule):
    severity = WARNING

    def apply(self, keyword):
        if not keyword.name == keyword.name.title():
            self.report(keyword, "Best practice is to Capitalize All The Words In A Keyword: " + keyword.name, keyword.linenumber)

class GlobalVariablesShouldBeUpperCase(GeneralRule):
    severity = WARNING

    def apply(self, robot_file):
        table = list(filter(lambda t: t.name.lower() == "variables", robot_file.tables))[0]
        for row in table.rows:
            if row.cells[0] != row.cells[0].upper():
                self.report(robot_file, "Variables in the \"Variables\" table should be UPPER CASE: " + row.cells[0], row.linenumber)

class TestCaseImplementation(TestRule):
    severity = ERROR

    def apply(self, test):
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(step[1].title())
        if test_steps != ALLOWED_KEYWORDS:
            self.report(test, "Check that you've refactored test case {} in right manner, expected: {}".format(test.name, ", ".join(ALLOWED_KEYWORDS)), test.linenumber)