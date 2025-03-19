import json
import requests
from nvbugs_api import NVBugsAPI

class TestMigration:
    def __init__(self, api_key):
        self.nvbugs_api = NVBugsAPI(api_key)

    def migrate_test_case(self, test_case):
        payload = json.dumps(test_case)
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{PROD_URL}/testcases", headers=headers, data=payload)
        if response.status_code == 201:
            return f"Test Case {test_case['id']} migrated successfully."
        else:
            return f"Failed to migrate Test Case {test_case['id']}."

    def process_keywords(self, keyword):
        test_cases = self.nvbugs_api.fetch_test_cases(keyword)
        if test_cases:
            for test_case in test_cases:
                result = self.migrate_test_case(test_case)
                print(result)
        else:
            print(f"No test cases found for keyword: {keyword}")