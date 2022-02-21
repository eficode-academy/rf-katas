from rflint.common import KeywordRule, SuiteRule, ERROR

from static import normalize

ALLOWED_KEYWORDS = [
    'Error Page Is Visible When Using Incorrect Credentials',
    'Verify That Error Page Is Visible'
]

class TestTemplateInUse(SuiteRule):
    severity = ERROR

    def apply(self, suite):
        is_test_template = False
        for setting in suite.settings:
            if setting[0].lower() == "test template":
                is_test_template = True
                if normalize(setting[1]) != ALLOWED_KEYWORDS[0]:
                    self.report(suite, f"Did you add correct keyword for test template?, expected: {ALLOWED_KEYWORDS[0]}", 0)
        if not is_test_template:
            self.report(suite, "Did you remember to add Test Template option?", 0)

class KeywordNamesIn07(SuiteRule):
    severity = ERROR

    def apply(self, suite):
        keywords = []
        for keyword in suite.keywords:
            keywords.append(keyword.name)
        if sorted(keywords) != ALLOWED_KEYWORDS:
            self.report(suite, f"Did you implement all keywords?, expected: {', '.join(ALLOWED_KEYWORDS)}", 0)

class TestTemplateImplementation(KeywordRule):
    severity = ERROR

    ALLOWED_TEMPLATE_STEPS = [
        'Enter Username',
        'Enter Password',
        'Submit Login Form',
        'Verify That Error Page Is Visible'
    ]

    def apply(self, keyword):
        if normalize(keyword.name) == ALLOWED_KEYWORDS[0]:
            steps = []
            for step in keyword.steps:
                if len(step) > 1:
                    steps.append(normalize(step[1]))
            if steps != self.ALLOWED_TEMPLATE_STEPS:
                self.report(keyword, f"Did you implement all needed steps for template?, expected: {', '.join(self.ALLOWED_TEMPLATE_STEPS)}", keyword.linenumber)