from rflint.common import KeywordRule, TestRule, ERROR
from static import normalize

MUST_KEYWORDS = [
    "Enter Username",
    "Enter Password",
    "Submit Login Form",
    "Verify That Error Page Is Visible"
]

SETUP_KEYWORD = "Open Browser To Login Page"


class KeywordImplementationRule05(KeywordRule):
    severity = ERROR

    def apply(self, keyword):
        report = False
        name = normalize(keyword.name)
        if name == MUST_KEYWORDS[0] or name == MUST_KEYWORDS[1]:
            if len(keyword.settings) == 0 or (not "[Arguments]" in keyword.settings[0]):
                report = True
        if report:
            self.report(keyword, "Did you remember to use keyword arguments?", keyword.linenumber)

class TestCaseImplementation05(TestRule):
    severity = ERROR

    def apply(self, test):
        default_message = f"Check that you've implemented test case {test.name} as instructed: "
        default_message += f"{SETUP_KEYWORD} is expected as a setup or part of the test. {', '.join(MUST_KEYWORDS)} are required as part of the test"
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(normalize(step[1]))
        has_failures = False
        if len(test_steps) == 5 and test_steps != [SETUP_KEYWORD] + MUST_KEYWORDS:
            has_failures = True
        elif len(test_steps) == 4:
            has_setup = False
            setup = next(filter(lambda s: "test setup" in str(s).lower(), test.parent.settings), "")
            if SETUP_KEYWORD in normalize(str(setup)) and not setup.is_comment():
                has_setup = True
            if not has_setup:
                for setting in test.settings:
                    s = normalize(str(setting))
                    if SETUP_KEYWORD in s and "[Setup]" in s:
                        has_setup = True
                        break

            if not has_setup:
                has_failures = True

        if has_failures:
            self.report(test, default_message, test.linenumber)
