from flask import Flask, request, jsonify
from test_migration import TestMigration
from bug_report import BugReporter

app = Flask(__name__)

API_KEY = "your-api-key"

migration_service = TestMigration(API_KEY)
bug_reporter = BugReporter(API_KEY)

@app.route("/migrate", methods=["POST"])
def migrate_tests():
    keyword = request.json.get("keyword")
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    migration_service.process_keywords(keyword)
    return jsonify({"message": f"Migration completed for keyword: {keyword}"}), 200

@app.route("/report-bugs", methods=["POST"])
def report_bugs():
    test_cases = request.json.get("test_cases")
    if not test_cases:
        return jsonify({"error": "Test cases are required"}), 400
    bug_reporter.analyze_and_report(test_cases)
    return jsonify({"message": "Bug reporting completed"}), 200

if __name__ == "__main__":
    app.run(debug=True)