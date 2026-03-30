
## Workshop 6

## Workshop Name: Validation, Verification, and CI with GitHub Action

## Description 

We will discuss validation, verification, and CI in the context of legal text understanding CFR document same as Assignment 5.

## Targeted Courses 

Software Quality Assurance 

## Activities 

### Pre-lab Content Dissemination 

**1. Validation:** Ensures the software meets customer requirements (i.e., “Are we building the right product?”). 

**2. Verification.** Ensures the software is built correctly according to specifications and design (i.e., “Are we building the product right?”).

**3. CI.** Software development practice where code changes are frequently merged into a shared repository and automatically built and tested to detect issues early.

We will use GitHub Actions to implement CI, catching issues early and maintaining code quality.



### In-class Hands-on Experience 
- Demo will be recorded and shared on CANVAS (Zoom Recordings).
- File Descriptions
    - `raw_regulations.txt`: Raw input of CFR or user requirements
    -  `requirements.json` : Transformed raw input into user requirements for SDLC. This file will
                             be used in validation and verification step to ensure user requirements.
    -  `test_cases.json`:    Test cases for verfication to ensure the software meets requirements.
    -  `expected_structure.json`: Used in validation step to ensure the software meets requirements.

    - `scripts\verfification.py` : Verfification script
    - `scripts\validation.py`    : Validation script
    - `.github/workflows/github-actions-SQAdemo.yml` : GitHub Actions workflow file for automating CI.


### Assignment 1 (Post Lab Experience) 





### Rubric
- Python source code [25%]
- Python test code [25%]
- Examples of test case failures [25%]
- Examples of test case successes [25%]

