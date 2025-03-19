from nvbugs_api import NVBugsAPI

class BugReporter:
    def __init__(self, api_key):
        self.nvbugs_api = NVBugsAPI(api_key)

    def analyze_and_report(self, test_cases):
        for test_case in test_cases:
            if test_case["status"] == "failed":
                issue_description = f"Test Case {test_case['id']} failed in production."
                response = self.nvbugs_api.report_bug(test_case["id"], issue_description)
                print(f"Bug reported: {response}")