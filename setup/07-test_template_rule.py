from rflint.common import KeywordRule, SuiteRule, TestRule, ERROR

ALLOWED_KEYWORDS = [
    'Template Error Page Is Visible When Using Incorrect Credentials',
    'Verify That Error Page Is Visible'
]

class TestTemplateInUse(SuiteRule):
    severity = ERROR


    def apply(self, suite):
        is_test_template = False
        for setting in suite.settings:
            if setting[0].lower() == "test template":
                is_test_template = True
                if setting[1].lower().title()  != ALLOWED_KEYWORDS[0]:
                    self.report(suite, "Did you add correct keyword for test template?, expected: {}".format(ALLOWED_KEYWORDS[1]), 0)
        if not is_test_template:
            self.report(suite, "Did you remember to add Test Template option?", 0)

class KeywordNamesIn07(SuiteRule):
    severity = ERROR

    def apply(self, suite):
        keywords = []
        for keyword in suite.keywords:
            keywords.append(keyword.name)
        if sorted(keywords) != ALLOWED_KEYWORDS:
            self.report(suite, "Did you implement all keywords?, expected: {}".format(", ".join(ALLOWED_KEYWORDS)), 0)

class TestTemplateImplementation(KeywordRule):
    severity = ERROR

    ALLOWED_TEMPLATE_STEPS = [
        'Enter Username',
        'Enter Password',
        'Submit Login Form',
        'Verify That Error Page Is Visible'
    ]

    def apply(self, keyword):
        if keyword.name.lower().title() == ALLOWED_KEYWORDS[0]:
            steps = []
            for step in keyword.steps:
                try:
                    steps.append(step[1].lower().title())
                except IndexError:
                    pass
            if steps != self.ALLOWED_TEMPLATE_STEPS:
                self.report(keyword, "Did you implement all needed steps for template?, expected: {}".format(", ".join(self.ALLOWED_TEMPLATE_STEPS)), keyword.linenumber)