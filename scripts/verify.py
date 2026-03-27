import json
import re
import sys

'''
1. Checks required fields exist


2. Checks ID format


3. Checks each requirement has at least one test case

'''

# Load requirements and test cases
with open("requirements.json") as f:
    requirements = json.load(f)

with open("test_cases.json") as f:
    test_cases = json.load(f)

test_ids = {t["requirement_id"] for t in test_cases}

failures = []

# Verification rules
for r in requirements:
    # Rule 1: Required fields
    for field in ["requirement_id", "description", "source"]:
        if field not in r:
            failures.append(f"Missing field '{field}' in requirement {r}")

    # Rule 2: ID format
    if not re.match(r"REQ-\d{3}[A-Z]", r["requirement_id"]):
        failures.append(f"Invalid requirement_id format: {r['requirement_id']}")

    # Rule 3: Must have at least one test case
    if r["requirement_id"] not in test_ids:
        failures.append(f"No test case for requirement: {r['requirement_id']}")

    # Rule 4: No vague phrase 
    if "all hazards" in r["description"].lower():
        failures.append(f"Vague description in requirement: {r['requirement_id']}")

    # Rule 5: Parent-child consistency 
    if "parent" in r and not r["requirement_id"].startswith(r["parent"]):
        failures.append(f"Parent-child ID mismatch: {r['requirement_id']} (parent {r['parent']})")

if failures:
    print("\n".join(failures))
    sys.exit(1)
else:
    print(" Verification passed: all requirements meet structural rules.")


