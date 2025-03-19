import requests

class NVBugsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://nvbugs.example.com/api"

    def fetch_test_cases(self, keyword):
        url = f"{self.base_url}/testcases?keyword={keyword}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    def report_bug(self, test_id, issue_description):
        url = f"{self.base_url}/report"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"test_id": test_id, "description": issue_description}
        response = requests.post(url, headers=headers, json=payload)
        return response.json() if response.status_code == 201 else None