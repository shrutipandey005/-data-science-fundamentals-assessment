"""
Unit Tests for Data Science Fundamentals Assessment
Self-contained runner that does not require optional unittest package.
"""

import math
import os
import sys

sys.path.append(os.path.dirname(__file__))

from statistical_toolkit import (
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_variance,
    calculate_std_dev,
    calculate_percentile,
    calculate_iqr,
    detect_outliers_iqr,
    calculate_pearson_correlation,
    bayes_theorem
)
from data_handler import DataSchemaValidator


def assert_almost_equal(a, b, places=4, msg=""):
    diff = abs(a - b)
    if diff > (10 ** -places):
        raise AssertionError(f"{msg}: {a} != {b} (diff: {diff})")


def run_all_tests():
    print("[*] Running Test Suite: Data Science Fundamentals...")
    tests_passed = 0

    # 1. Test Mean
    assert calculate_mean([1, 2, 3, 4, 5]) == 3.0, "Failed mean test 1"
    assert calculate_mean([2, 4, 4, 4, 5, 5, 7, 9]) == 5.0, "Failed mean test 2"
    tests_passed += 1
    print("  [PASS] Test Mean: Passed")

    # 2. Test Median
    assert calculate_median([1, 3, 5]) == 3.0, "Failed odd median test"
    assert calculate_median([1, 2, 3, 4]) == 2.5, "Failed even median test"
    tests_passed += 1
    print("  [PASS] Test Median: Passed")

    # 3. Test Mode
    sample = [2, 4, 4, 4, 5, 5, 7, 9]
    assert calculate_mode(sample) == [4], "Failed unimodal test"
    assert set(calculate_mode([1, 1, 2, 2, 3])) == {1, 2}, "Failed multimodal test"
    tests_passed += 1
    print("  [PASS] Test Mode: Passed")

    # 4. Test Variance & Std Dev
    # [1, 2, 3, 4, 5]: mean=3. sq diff sum = 4 + 1 + 0 + 1 + 4 = 10.
    # sample var = 10 / 4 = 2.5; pop var = 10 / 5 = 2.0
    assert_almost_equal(calculate_variance([1, 2, 3, 4, 5], sample=True), 2.5)
    assert_almost_equal(calculate_variance([1, 2, 3, 4, 5], sample=False), 2.0)
    assert_almost_equal(calculate_std_dev([1, 2, 3, 4, 5], sample=True), math.sqrt(2.5))
    tests_passed += 1
    print("  [PASS] Test Variance & Std Dev: Passed")

    # 5. Test Percentiles & IQR
    data = [10, 20, 30, 40, 50]
    assert calculate_percentile(data, 0) == 10.0
    assert calculate_percentile(data, 50) == 30.0
    assert calculate_percentile(data, 100) == 50.0
    q1, q3, iqr = calculate_iqr(data)
    assert q1 == 20.0 and q3 == 40.0 and iqr == 20.0
    tests_passed += 1
    print("  [PASS] Test Percentiles & IQR: Passed")

    # 6. Test Outlier Detection
    outlier_res = detect_outliers_iqr([10, 12, 11, 13, 12, 100])
    assert 100 in outlier_res["outliers"]
    assert 12 not in outlier_res["outliers"]
    tests_passed += 1
    print("  [PASS] Test Outlier Detection: Passed")

    # 7. Test Pearson Correlation
    x = [1, 2, 3, 4, 5]
    y_pos = [2, 4, 6, 8, 10]
    assert_almost_equal(calculate_pearson_correlation(x, y_pos), 1.0)
    y_neg = [10, 8, 6, 4, 2]
    assert_almost_equal(calculate_pearson_correlation(x, y_neg), -1.0)
    tests_passed += 1
    print("  [PASS] Test Pearson Correlation: Passed")

    # 8. Test Bayes' Theorem
    post = bayes_theorem(0.01, 0.99, 0.05)
    assert_almost_equal(post, 1/6, places=5)
    tests_passed += 1
    print("  [PASS] Test Bayes' Theorem: Passed")

    # 9. Test Data Schema Parsing
    raw = {
        "customer_id": "CUST-999",
        "signup_date": "2023-05-10",
        "tenure_months": "15",
        "monthly_charges": "49.99",
        "total_charges": "749.85",
        "contract_type": "Month-to-month",
        "satisfaction_tier": "High",
        "support_tickets": "2",
        "feedback_notes": "Great experience overall",
        "churned": "0"
    }
    parsed = DataSchemaValidator.transform_churn_record(raw)
    assert parsed["customer_id"] == "CUST-999"
    assert parsed["tenure_months"] == 15
    assert parsed["monthly_charges"] == 49.99
    assert parsed["satisfaction_tier_numeric"] == 3
    assert parsed["churned"] == 0
    tests_passed += 1
    print("  [PASS] Test Schema Parsing: Passed")

    print("\n==========================================")
    print(f" ALL {tests_passed} UNIT TESTS PASSED SUCCESSFULLY!")
    print("==========================================")


if __name__ == "__main__":
    run_all_tests()
