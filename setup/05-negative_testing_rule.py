from rflint.common import KeywordRule, SuiteRule, TestRule, ERROR

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
        name = keyword.name.lower().title()
        if name == MUST_KEYWORDS[0] or name == MUST_KEYWORDS[1]:
            if len(keyword.settings) == 0 or (not "[Arguments]" in keyword.settings[0]):
                report = True
        if report:
            self.report(keyword, "Did you remember to use keyword arguments?", keyword.linenumber)

class TestCaseImplementation05(TestRule):
    severity = ERROR

    def apply(self, test):
        default_message = "Check that you've implemented test case {} as instructed: ".format(test.name)
        default_message += "{} is expected as a setup or part of the test. {} are required as part of the test".format(SETUP_KEYWORD, ", ".join(MUST_KEYWORDS))
        test_steps = []
        for step in test.steps:
            if len(step) > 1:
                test_steps.append(step[1].lower().title())
        is_report = False
        if len(test_steps) == 5 and test_steps != [SETUP_KEYWORD] + MUST_KEYWORDS:
            is_report = True
        elif len(test_steps) == 4:
            has_setup = False
            setup = list(filter(lambda s: "test setup" in str(s).lower(), test.parent.settings))[0]
            if SETUP_KEYWORD.lower() in str(setup).lower() and not setup.is_comment():
                has_setup = True
            if not has_setup:
                for setting in test.settings:
                    s = str(setting).lower()
                    if SETUP_KEYWORD.lower() in s and "[setup]" in s:
                        has_setup = True
                        break

            if not has_setup:
                is_report = True

        if is_report:
            self.report(test, default_message, test.linenumber)
