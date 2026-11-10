#!/usr/bin/env python3
"""
Data Science Fundamentals Assessment - Unified Project Entry Point
Author: Data Science Pair Programmer
Date: 2026-11-10

This script provides an interactive and automated CLI entry point to:
  1. Validate the execution environment (Python 3.8+)
  2. Execute the complete 9-point statistical & data handler test suite
  3. Execute the full 6-objective Data Science Fundamentals Assessment runner
  4. Generate and verify project outputs, notebooks, and reports
"""

import os
import sys
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, "notebooks")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")

# Add src to path
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


def print_banner(text: str):
    print("\n" + "=" * 76)
    print(f"  {text}")
    print("=" * 76)


def main():
    print_banner("DATA SCIENCE FUNDAMENTALS ASSESSMENT - UNIFIED RUNNER")
    print(f"[*] Workspace Root: {PROJECT_ROOT}")
    print(f"[*] Python Runtime: {sys.executable} (Version: {sys.version.split()[0]})")
    
    # Step 1: Run Unit Tests
    print_banner("STEP 1: EXECUTING UNIT TEST SUITE (test_fundamentals.py)")
    test_script = os.path.join(SRC_DIR, "test_fundamentals.py")
    res_tests = subprocess.run([sys.executable, test_script], cwd=PROJECT_ROOT)
    if res_tests.returncode != 0:
        print("[!] Unit tests failed with return code:", res_tests.returncode)
        sys.exit(res_tests.returncode)

    # Step 2: Run Full Assessment
    print_banner("STEP 2: EXECUTING FULL ASSESSMENT (fundamentals_assessment.py)")
    assessment_script = os.path.join(SRC_DIR, "fundamentals_assessment.py")
    res_assessment = subprocess.run([sys.executable, assessment_script], cwd=PROJECT_ROOT)
    if res_assessment.returncode != 0:
        print("[!] Assessment failed with return code:", res_assessment.returncode)
        sys.exit(res_assessment.returncode)

    # Step 3: Project Summary & Artifact Verification
    print_banner("STEP 3: ASSESSMENT DELIVERABLES VERIFICATION")
    artifacts = [
        ("Structured Report", os.path.join(REPORTS_DIR, "Data_Science_Fundamentals_Report.md")),
        ("Jupyter Notebook", os.path.join(NOTEBOOKS_DIR, "Data_Science_Fundamentals_Assessment.ipynb")),
        ("Customer Churn CSV", os.path.join(PROJECT_ROOT, "data", "customer_churn_analysis.csv")),
        ("E-Commerce Orders JSON", os.path.join(PROJECT_ROOT, "data", "ecommerce_orders.json")),
    ]

    all_exist = True
    for name, path in artifacts:
        status = "[FOUND]" if os.path.exists(path) else "[MISSING]"
        size = f"({os.path.getsize(path)} bytes)" if os.path.exists(path) else ""
        print(f"  {status} {name:24} : {path} {size}")
        if not os.path.exists(path):
            all_exist = False

    if all_exist:
        print_banner("ALL ASSESSMENT DELIVERABLES & OBJECTIVES READY TO SUBMIT!")
        print("  [>] Open in VS Code to review code, test files, and notebooks.")
        print("  [>] Push to GitHub using: git remote add origin <your-repo-url> && git push -u origin main\n")


if __name__ == "__main__":
    main()

