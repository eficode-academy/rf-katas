from rflint.common import KeywordRule, TestRule, GeneralRule, ERROR, WARNING
from static import normalize

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
        if not normalize(keyword.name) in ALLOWED_KEYWORDS:
            self.report(keyword, f"Keyword {keyword.name} not allowed in {', '.join(ALLOWED_KEYWORDS)}", keyword.linenumber)

class KeywordImplementation(KeywordRule):
    severity = ERROR

    def apply(self, keyword):
        report = False
        if normalize(keyword.name) == ALLOWED_KEYWORDS[0]:
            if not "${URL}" in keyword.steps[1][2].upper():
                report = True
        if report:
            self.report(keyword, f"Do you have URL variable in place? Check keyword: {ALLOWED_KEYWORDS[0]}", keyword.linenumber+1)

class KeywordsShouldStartWithCapitalLetter(KeywordRule):
    severity = WARNING

    def apply(self, keyword):
        if not keyword.name == normalize(keyword.name):
            self.report(keyword, f"Best practice is to Capitalize All The Words In A Keyword: {keyword.name}", keyword.linenumber)

class GlobalVariablesShouldBeUpperCase(GeneralRule):
    severity = WARNING

    def apply(self, robot_file):
        table = list(filter(lambda t: t.name.lower() == "variables", robot_file.tables))
        if table:
            table=table[0]
            for row in table.rows:
                if row.cells[0] != row.cells[0].upper():
                    self.report(robot_file, f"Variables in the \"Variables\" table should be UPPER CASE: {row.cells[0]}", row.linenumber)
        else:
            self.report(robot_file, "login.robot is missing variables table.", 0)

class TestCaseImplementation(TestRule):
    severity = ERROR

    def apply(self, test):
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(normalize(step[1]))
        if test_steps != ALLOWED_KEYWORDS:
            self.report(test, f"Check that you've refactored test case {test.name} in right manner, expected: {', '.join(ALLOWED_KEYWORDS)}", test.linenumber)
