import pytest
import json
from code.main_pipeline import SecureRefactoringPipeline

@pytest.fixture
def pipeline():
    return SecureRefactoringPipeline()

def test_safe_refactoring(pipeline):
    res = pipeline.process_command("Invoke-Expression 'Get-Process'", "List processes securely")
    assert res["compliance_status"] in ["COMPLIANT", "NON_COMPLIANT"]
    assert res["risk_score"] >= 0

def test_adversarial_robustness(pipeline):
    with open("tests/adversarial_cases.json", "r") as f:
        cases = json.load(f)
    blocked = 0
    false_positives = 0
    for c in cases:
        res = pipeline.process_command(c["input"], "test")
        if c["expected_block"] and res.get("status") == "BLOCKED":
            blocked += 1
        if not c["expected_block"] and res.get("status") == "BLOCKED":
            false_positives += 1
            
    assert blocked == 2, "Failed to block known attack vectors"
    assert false_positives == 0, "False positive on benign input"