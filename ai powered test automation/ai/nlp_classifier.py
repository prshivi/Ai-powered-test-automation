from transformers import pipeline

classifier = pipeline("zero-shot-classification")

def categorize_test_case(description):
    labels = ["UI Bug", "Backend Issue", "Performance Bug"]
    result = classifier(description, labels)
    return result["labels"][0]