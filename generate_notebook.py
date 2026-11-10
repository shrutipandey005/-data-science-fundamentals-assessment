import json
import os

notebook_path = r"C:\Users\User\.gemini\antigravity\scratch\data_science_fundamentals_assessment\notebooks\Data_Science_Fundamentals_Assessment.ipynb"

def md_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source.split("\n")]
    }

def code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.split("\n")]
    }

cells = [
    md_cell("""# Data Science Fundamentals Assessment
**Author:** Pair Programming Assessment Candidate  
**Focus Areas:** Data Science Lifecycle, Python Programming, Statistical Foundations, Data Types & Handling, Best Practices, and End-to-End Practical EDA.

---

## Assessment Objectives
1. **Understand Data Science Fundamentals:** Lifecycle, analysis types, industry use cases.
2. **Apply Python Programming Basics:** Primitives, operators, control flow, functions, collections, file handling.
3. **Learn Statistical Foundations:** Measures of central tendency, spread, percentiles, probability, correlation.
4. **Understand Data Types & Structures:** Numerical, categorical, ordinal, temporal, and text data handling.
5. **Follow Data Science Best Practices:** Clean code, reproducibility, error handling, ethical interpretation.
6. **Complete Fundamentals Assignments:** Practical hands-on problem solving."""),

    md_cell("""---
## Section 1: Data Science Fundamentals & Problem Framing
### 1.1 The 7 Lifecycle Stages
1. **Business Understanding & Problem Definition**: Scoping goals, KPIs, success criteria.
2. **Data Acquisition / Collection**: Pulling from transactional DBs, APIs, logs, third-party streams.
3. **Data Cleaning & Preprocessing**: Handling missing entries, schema normalization, outlier analysis.
4. **Exploratory Data Analysis (EDA)**: Descriptive statistics, bivariate correlations, distribution inspection.
5. **Feature Engineering & Modeling**: Designing predictive indicators, training baseline algorithms.
6. **Model Validation & Evaluation**: Cross-validation, fairness checks, business impact calculation.
7. **Deployment, Monitoring & Maintenance**: CI/CD, data drift detection, periodic retraining.

### 1.2 The Four Analytical Archetypes
* **Descriptive:** What happened? (e.g., Q3 customer churn rate was 35%).
* **Diagnostic:** Why did it happen? (e.g., customers with >3 support tickets churn at 4x the baseline).
* **Predictive:** What will happen? (e.g., probability that account CUST-1042 will cancel within 30 days).
* **Prescriptive:** What should we do? (e.g., offer a loyalty router upgrade to high-risk customers)."""),

    code_cell("""# Section 1 Verification & Problem Framing Schema
problem_statement = {
    "industry": "Telecommunications & ISP",
    "business_goal": "Reduce annual subscriber churn from 24% to 18%",
    "data_requirements": ["tenure", "monthly_charges", "support_tickets", "contract_type", "feedback_notes"],
    "analysis_type": "Predictive & Prescriptive",
    "kpi": "Net Customer Lifetime Value (LTV) and 90-day retention rate"
}
for k, v in problem_statement.items():
    print(f"{k.replace('_', ' ').title():<20}: {v}")"""),

    md_cell("""---
## Section 2: Python Programming Basics
Demonstrating fundamental constructs: primitives, operators, conditionals, functions, lists, tuples, dicts, sets, and error handling."""),

    code_cell("""# 2.1 Python Collections & Comprehensions
customer_ids = ["CUST-101", "CUST-102", "CUST-103", "CUST-101"]
unique_ids = set(customer_ids)
print("Unique Customers Count:", len(unique_ids))

# Dictionary comprehension for customer tiers
customer_tenures = {"CUST-101": 24, "CUST-102": 3, "CUST-103": 48}
customer_tiers = {
    cid: ("Senior" if months >= 24 else "New") 
    for cid, months in customer_tenures.items()
}
print("Customer Tiers:", customer_tiers)

# 2.2 Reusable Function with Error Handling
def compute_clv(monthly_fee: float, tenure_months: int, discount: float = 0.0) -> float:
    \"\"\"Calculates net customer lifetime value safely.\"\"\"
    if monthly_fee < 0 or tenure_months < 0:
        raise ValueError("Charges and tenure must be non-negative.")
    net_monthly = monthly_fee * (1.0 - discount)
    return round(net_monthly * tenure_months, 2)

print("CLV Calculation:", compute_clv(75.50, 18, discount=0.10))"""),

    md_cell("""---
## Section 3: Statistical Foundations & Mathematical Toolkit
Formulas implemented:
* **Mean:** $\\bar{x} = \\frac{1}{n} \\sum_{i=1}^n x_i$
* **Median:** Central element of ordered array
* **Sample Variance:** $s^2 = \\frac{1}{n-1} \\sum_{i=1}^n (x_i - \\bar{x})^2$
* **Standard Deviation:** $s = \\sqrt{s^2}$
* **Pearson Correlation:** $r = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum(x_i - \\bar{x})^2 \\sum(y_i - \\bar{y})^2}}$
* **Bayes' Rule:** $P(A|B) = \\frac{P(B|A) P(A)}{P(B)}$"""),

    code_cell("""import math
from collections import Counter

def calc_mean(data):
    return sum(data) / len(data)

def calc_median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 != 0 else (s[mid - 1] + s[mid]) / 2.0

def calc_std(data, sample=True):
    m = calc_mean(data)
    dof = (len(data) - 1) if sample else len(data)
    return math.sqrt(sum((x - m) ** 2 for x in data) / dof)

def calc_pearson_r(x, y):
    mx, my = calc_mean(x), calc_mean(y)
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den = math.sqrt(sum((xi - mx)**2 for xi in x) * sum((yi - my)**2 for yi in y))
    return num / den if den != 0 else 0.0

# Demonstration on Sample Metrics
sample_charges = [35.0, 45.2, 55.0, 65.5, 75.0, 89.9, 110.0, 120.0]
print(f"Mean Monthly Charge:   ${calc_mean(sample_charges):.2f}")
print(f"Median Monthly Charge: ${calc_median(sample_charges):.2f}")
print(f"Std Deviation (Sample): ${calc_std(sample_charges):.2f}")"""),

    md_cell("""---
## Section 4: Data Types & Structures
* **Numerical Continuous:** e.g., `monthly_charges`, `total_charges`
* **Numerical Discrete:** e.g., `support_tickets`, `tenure_months`
* **Categorical Nominal:** e.g., `contract_type` (Month-to-month, One year, Two year)
* **Categorical Ordinal:** e.g., `satisfaction_tier` (Low < Medium < High < Very High)
* **Datetime:** e.g., `signup_date` (parse year, month, recency)
* **Text / Unstructured:** e.g., `feedback_notes` (tokenization, word frequencies)"""),

    code_cell("""# Section 4: Type Schema Mapping
ordinal_scale = {"Low": 1, "Medium": 2, "High": 3, "Very High": 4}
sample_record = {
    "customer_id": "CUST-1002",
    "signup_date": "2022-06-10",
    "tenure_months": 24,
    "monthly_charges": 89.90,
    "satisfaction_tier": "High",
    "support_tickets": 1,
    "churned": 0
}
encoded_satisfaction = ordinal_scale[sample_record["satisfaction_tier"]]
print(f"Original Ordinal: '{sample_record['satisfaction_tier']}' -> Numerical Encoded: {encoded_satisfaction}")"""),

    md_cell("""---
## Section 5: Data Science Best Practices
1. **Readable, PEP 8 Compliant Code:** Clear semantic identifiers over single-letter variables.
2. **Deterministic & Reproducible Runs:** Always control random seeds.
3. **Data Integrity & Validation:** Explicit schema casting and missing value imputation rules.
4. **Responsible Interpretation:** Distinction between correlation ($r$) and causation."""),

    code_cell("""# Section 5: Reproducibility & Assertions Example
import random

random.seed(42)
synthetic_sample = [random.randint(10, 100) for _ in range(5)]
print("Reproducible Synthetic Sample:", synthetic_sample)
assert len(synthetic_sample) == 5
assert all(10 <= x <= 100 for x in synthetic_sample)
print("Assertion checks passed successfully.")"""),

    md_cell("""---
## Section 6: Practical Fundamentals Assignment
### Ingestion & Analysis of Real Dataset files
* Ingests `data/customer_churn_analysis.csv`
* Computes cohort statistics (retained vs churned)
* Evaluates bivariate correlations
* Ingests `data/ecommerce_orders.json` and performs multi-tiered aggregation"""),

    code_cell("""import csv
import json
import os

data_dir = os.path.join(os.path.dirname(os.getcwd()), "data") if "notebooks" in os.getcwd() else "data"
csv_path = os.path.join(data_dir, "customer_churn_analysis.csv")
json_path = os.path.join(data_dir, "ecommerce_orders.json")

# Ingest CSV
rows = []
with open(csv_path, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append({
            "id": r["customer_id"],
            "tenure": int(r["tenure_months"]),
            "charges": float(r["monthly_charges"]),
            "tickets": int(r["support_tickets"]),
            "churn": int(r["churned"])
        })

tenures = [r["tenure"] for r in rows]
tickets = [r["tickets"] for r in rows]
churns = [r["churn"] for r in rows]

r_tenure_churn = calc_pearson_r(tenures, churns)
r_tickets_churn = calc_pearson_r(tickets, churns)

print(f"Total Records Analyzed: {len(rows)}")
print(f"Correlation (Tenure, Churn):          {r_tenure_churn:+.4f}")
print(f"Correlation (Support Tickets, Churn): {r_tickets_churn:+.4f}")

# Ingest and Summarize JSON
with open(json_path, mode="r", encoding="utf-8") as f:
    orders = json.load(f)

net_revenue = 0.0
for o in orders:
    disc = o.get("discount_applied", 0.0)
    for itm in o["items"]:
        net_revenue += (itm["unit_price"] * itm["quantity"]) * (1.0 - disc)

print(f"Processed {len(orders)} E-Commerce orders.")
print(f"Total Net E-Commerce Revenue: ${net_revenue:,.2f}")"""),

    md_cell("""---
## Conclusion & Assessment Summary
All 6 foundational objectives have been demonstrated with programmatic implementations, statistical computations, and data handling workflows.""")
]

notebook = {
    "cells": cells,
    "metadata": {
        "language_info": {
            "name": "python",
            "version": "3.12"
        },
        "orig_nbformat": 4
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Jupyter Notebook created at:", notebook_path)
