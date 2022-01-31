from rflint.common import SuiteRule, ResourceRule, ERROR

class ResourceFileInUse(SuiteRule):
    severity = ERROR

    def apply(self, suite):
        has_resources = False
        for setting in suite.settings:
            if setting[0].lower() == "resource":
                has_resources = True
        if not has_resources:
            self.report(suite, "Did you remember to add resource to settings?", 0)

class NumberOfKeywordsInSuite06(SuiteRule):
    severity = ERROR

    def apply(self, suite):
        keywords = []
        report = False
        for keyword in suite.keywords:
            keywords.append(keyword.name)
        if suite.name == "login" and len(keywords) != 4:
            report = True
        elif suite.name == "invalid_login" and len(keywords) != 1:
            report = True
        if report:
            self.report(suite, "Did you remove only those keywords that are shared between login.robot and invalid_login.robot?", 0)

class NumberOfKeywordsInResource06(ResourceRule):
    severity = ERROR
    ALLOWED_KEYWORDS = [
        'Open Browser To Login Page',
        'Enter Username',
        'Enter Password',
        'Submit Login Form'
    ]
    def apply(self, resource):
        keywords = []
        for keyword in resource.keywords:
            keywords.append(keyword.name.lower().title())
        if keywords != self.ALLOWED_KEYWORDS:
            self.report(resource, f"Did you remember to add all keywords: {', '.join(self.ALLOWED_KEYWORDS)} to common.resource file?", 0)

class NumberOfTestCasesInSuite06(SuiteRule):
    severity = ERROR

    def apply(self, suite):
        tests = []
        for test in suite.testcases:
            tests.append(test.name)
        if suite.name == "login" and len(tests) != 2:
            self.report(suite, "Do you have the existing 2 cases in login.robot?", 0)
        elif suite.name == "invalid_login" and len(tests) != 3:
            self.report(suite, "Did you implement 2 more tests to invalid_login.robot?", 0)
