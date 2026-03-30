
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

- Navigate to 
- 
- Demo will be recorded and shared on CANVAS (Zoom Recordings). 



### Assignment 1 (Post Lab Experience) 

- For this part of the workshop you will develop two Python program files to demonstrate that you have practiced test-driven development (TDD). 
- Your code should satisfy the following requirements:
  - The calculator must be able to multiply and divide
  - The calculator must be able to find square root of a number
  - All methods related to mathematical operations should handle division by zero exceptions
  - Written code has been scanned by a static analysis tool. You will apply static analysis to your Python program files. Use the [Bandit](https://bandit.readthedocs.io/en/latest/) tool to perform static analysis and report any weaknesses that you find in a TEXT file
- Submit your Python program files and  your TEXT file on CANVAS @ `Assignment 1`
- Due: Feb 09, 2025


### Commands that you can find useful
- `pip install bandit` to install bandit 
- `bandit -r <FOLDER_PATH_OF_YOUR_CODE>`

### Rubric
- Python source code [25%]
- Python test code [25%]
- Examples of test case failures [25%]
- Examples of test case successes [25%]

