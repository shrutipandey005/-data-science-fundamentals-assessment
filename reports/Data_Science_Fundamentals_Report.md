# Data Science Fundamentals Assessment Report

**Candidate / Role:** Advanced Data Science Candidate  
**Assessment Date:** November 10, 2026  
**Artifact Directory:** `scratch/data_science_fundamentals_assessment`  
**Execution Environment:** Python 3.12 Standard Environment  

---

## Executive Summary

This comprehensive assessment report documents the mastery and end-to-end application of core Data Science fundamentals across six core dimensions:
1. **Data Science Methodology & Lifecycle**
2. **Python Programming Foundations**
3. **Statistical Foundations & Probability**
4. **Data Types & Feature Representation**
5. **Data Science Best Practices & Ethics**
6. **Practical Hands-on Analytics Assignments**

All code snippets and data workflows have been verified and executed against realistic datasets (`data/customer_churn_analysis.csv` and `data/ecommerce_orders.json`) with an accompanying unit-tested codebase in `src/` and a self-contained Jupyter Notebook in `notebooks/`.

---

## Objective 1: Data Science Fundamentals & Problem Framing

### 1.1 The End-to-End Data Science Lifecycle
The Data Science lifecycle is an iterative, hypothesis-driven workflow transforming raw signals into actionable organizational decisions:

```
[1. Problem Formulation] ──> [2. Data Acquisition] ──> [3. Data Cleansing & ETL]
         ▲                                                      │
         │                                                      ▼
[7. Monitoring & Drift] <── [6. Model Evaluation] <── [5. Modeling] <── [4. Exploratory EDA]
```

1. **Problem Definition (Business Understanding):** Translate ambiguous business inquiries into quantitative objectives, specifying target metrics (e.g., reduce customer churn rate by 15%), constraints, and success thresholds.
2. **Data Collection & Ingestion:** Extracting structured, semi-structured, and unstructured data from transactional databases (SQL), telemetry logs, event buses (Kafka), RESTful APIs, and cloud buckets.
3. **Data Cleaning & Preparation:** Handling missing values, schema coercion, deduplication, outlier auditing, and normalizations.
4. **Exploratory Data Analysis (EDA):** Computing summary statistics, uncovering patterns, testing distributional assumptions, and detecting bivariate correlations.
5. **Feature Engineering & Modeling:** Formulating predictive features (ratios, aggregations, encodings) and selecting appropriate statistical or machine learning models.
6. **Validation & Evaluation:** Measuring generalization with cross-validation, offline metrics (Precision, Recall, ROC-AUC, RMSE), bias audits, and A/B test experiments.
7. **Deployment & Governance:** Serving models via microservices/APIs, continuous integration/continuous deployment (CI/CD), pipeline logging, and real-time concept drift monitoring.

---

### 1.2 The Four Archetypes of Data Analysis

| Analysis Archetype | Core Question | Primary Techniques | Industry Telecom Example |
| :--- | :--- | :--- | :--- |
| **Descriptive** | *What happened?* | Summary statistics, aggregation, reporting, dashboards | "The churn rate for the current quarter was 35.0%." |
| **Diagnostic** | *Why did it happen?* | Root cause analysis, cohort drills, correlation, hypothesis tests | "Churned subscribers experienced an average of 4.29 support tickets vs 1.00 for retained customers." |
| **Predictive** | *What will happen?* | Supervised ML classification, time-series forecasting, regression | "Customer CUST-1003 has an 82% predicted probability of churn within 30 days." |
| **Prescriptive** | *What should we do?* | Optimization algorithms, uplift modeling, decision rules | "Offer CUST-1003 an expedited router replacement and a \$15 loyalty discount to lower churn likelihood to 18%." |

---

### 1.3 Real-World Industry Use Cases

1. **Healthcare & Life Sciences:** Diagnostic imaging anomaly detection, patient readmission prediction, and randomized clinical trial validation.
2. **FinTech & Banking:** Real-time credit card fraud detection (unsupervised anomaly scoring), credit risk underwriting, and algorithmic portfolio allocation.
3. **E-Commerce & Retail:** Dynamic pricing optimization, personalized recommendation systems (collaborative filtering), and supply chain demand forecasting.
4. **Telecommunications:** Network congestion forecasting, cell tower latency diagnosis, and customer churn intervention.

---

## Objective 2: Python Programming Basics for Data Science

Python serves as the lingua franca of Data Science. The table below details foundational structures and their specific data science application:

### 2.1 Core Data Structures & Operations

```python
# 1. Primitives & Conditionals
tenure = 18
is_retained = True if tenure >= 12 else False

# 2. Collections Comparison
feature_list = ["tenure", "monthly_charges", "support_tickets", "monthly_charges"] # Mutable, allows duplicates
feature_set = set(feature_list)     # Unique elements: {'tenure', 'monthly_charges', 'support_tickets'}
schema_tuple = ("id", "date", "y")  # Immutable sequence ensuring fixed schema order

# 3. Dictionaries for Entity Representation
customer_profile = {
    "customer_id": "CUST-1002",
    "monthly_charges": 89.90,
    "tier": "High"
}

# 4. List and Dictionary Comprehensions
discounts = [round(price * 0.9, 2) for price in [29.99, 45.20, 89.90, 110.00]]
tier_map = {row["customer_id"]: row["tier"] for row in [customer_profile]}
```

### 2.2 Defensive Function Design & Error Handling
```python
def safe_ratio(numerator: float, denominator: float, fallback: float = 0.0) -> float:
    """Computes division safely, guarding against ZeroDivisionError and NaN."""
    try:
        if math.isnan(numerator) or math.isnan(denominator):
            return fallback
        return numerator / denominator
    except ZeroDivisionError:
        return fallback
```

---

## Objective 3: Statistical Foundations & Mathematical Formulations

### 3.1 Measures of Central Tendency

* **Arithmetic Mean ($\bar{x}$):**
  $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$
  *Properties:* Sensitive to extreme outliers. For instance, in our sample dataset `[12, 15, 18, 20, 22, 22, 24, 25, 28, 30, 32, 95]`, the mean is **28.58**, pulled substantially upward by the outlier **95**.

* **Median ($\tilde{x}$):**
  The middle observation when values are sorted in ascending order.
  $$\tilde{x} = 23.00$$
  *Properties:* Resistant / robust to extreme skewness and outliers.

* **Mode:**
  The value that appears with the highest frequency. In our sample data, the mode is **22** (frequency = 2).

---

### 3.2 Measures of Dispersion & Bessel's Correction

* **Sample Variance ($s^2$) vs Population Variance ($\sigma^2$):**
  $$s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2, \quad \sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2$$
  *Why $n - 1$ (Bessel's Correction)?* Dividing by $n$ underestimates population variance because sample points are naturally closer to their sample mean than the true unknown population mean $\mu$. Using $n-1$ yields an unbiased estimator ($E[s^2] = \sigma^2$).
  *Computed Values on Sample Data:*
  * Sample Variance $s^2 = \mathbf{471.90}$
  * Population Variance $\sigma^2 = \mathbf{432.58}$
  * Sample Standard Deviation $s = \sqrt{s^2} = \mathbf{21.72}$

---

### 3.3 Percentiles, Interquartile Range (IQR), and Tukey's Outlier Fences

* **First Quartile ($Q_1$ / 25th percentile):** $19.50$
* **Third Quartile ($Q_3$ / 75th percentile):** $28.50$
* **Interquartile Range ($IQR$):**
  $$IQR = Q_3 - Q_1 = 28.50 - 19.50 = \mathbf{9.00}$$
* **Tukey's Fences:**
  $$\text{Lower Fence} = Q_1 - 1.5 \times IQR = 19.50 - 13.50 = \mathbf{6.00}$$
  $$\text{Upper Fence} = Q_3 + 1.5 \times IQR = 28.50 + 13.50 = \mathbf{42.00}$$
  *Result:* Values outside $[6.00, 42.00]$ are flagged as outliers. The value **95** is formally detected as an upper outlier.

---

### 3.4 Bivariate Association: Pearson Correlation Coefficient ($r$)

$$r_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}$$

*Range:* $-1.0 \le r \le +1.0$
* Sign indicates direction (positive = direct, negative = inverse).
* Magnitude indicates linear strength ($|r| > 0.7$ denotes strong linear association).

---

### 3.5 Probability Fundamentals & Bayes' Theorem

$$\mathbb{P}(A \mid B) = \frac{\mathbb{P}(B \mid A) \cdot \mathbb{P}(A)}{\mathbb{P}(B)} = \frac{\mathbb{P}(B \mid A) \cdot \mathbb{P}(A)}{\mathbb{P}(B \mid A)\mathbb{P}(A) + \mathbb{P}(B \mid \neg A)\mathbb{P}(\neg A)}$$

*Practical Scenario:*
* Prior probability that an email is spam: $\mathbb{P}(\text{Spam}) = 0.20$
* Likelihood of keyword "Free" in spam: $\mathbb{P}(\text{Free} \mid \text{Spam}) = 0.80$
* False alarm likelihood in legitimate email: $\mathbb{P}(\text{Free} \mid \text{Ham}) = 0.05$
* Posterior probability $\mathbb{P}(\text{Spam} \mid \text{Free})$:
  $$\mathbb{P}(\text{Spam} \mid \text{Free}) = \frac{0.80 \times 0.20}{(0.80 \times 0.20) + (0.05 \times 0.80)} = \frac{0.16}{0.16 + 0.04} = \frac{0.16}{0.20} = \mathbf{80.0\%}$$

---

## Objective 4: Data Types & Structures in Real Analysis

| Statistical Data Type | Machine Representation | Concrete Feature | Appropriate Handling / Transformation |
| :--- | :--- | :--- | :--- |
| **Numerical Continuous** | `float` | `monthly_charges` (\$78.34) | Standardization ($z$-score), MinMax scaling, log-transform if skewed |
| **Numerical Discrete** | `int` | `support_tickets` (0, 1, 2, ...) | Count-based distributions (Poisson, Negative Binomial), capping |
| **Categorical Nominal** | `str` | `contract_type` (Month-to-month, ...) | One-Hot Encoding (binary dummy indicators), frequency encoding |
| **Categorical Ordinal** | `str` / `int` | `satisfaction_tier` (Low < Med < High) | Monotonic integer mapping (`Low`: 1, `Medium`: 2, `High`: 3, `Very High`: 4) |
| **Temporal / Datetime** | `datetime.date` | `signup_date` (2023-01-15) | Decomposition: `day_of_week`, `quarter`, `tenure_days` recency |
| **Text / Unstructured** | `str` | `feedback_notes` | Lowercasing, punctuation stripping, tokenization, n-grams, TF-IDF |

---

## Objective 5: Data Science Best Practices

1. **Meaningful Semantic Identifiers:** Avoid cryptic variable names like `x1`, `temp`, `df2`. Favor descriptive names: `monthly_subscriber_charges`, `churn_risk_score`.
2. **Deterministic Reproducibility:** Ensure seeds are fixed for pseudo-random generators (`random.seed(42)`).
3. **Graceful Schema Coercion & Imputation:** Never drop records blindly without auditing missingness mechanisms (MCAR vs MAR vs MNAR). Document all imputation rules.
4. **Separation of Concerns:** Keep raw data immutable in `data/`, business logic in modular scripts in `src/`, exploratory narratives in `notebooks/`, and final deliverables in `reports/`.
5. **Responsible Analytical Interpretation:**
   * **Correlation does not equal Causation:** A high correlation between support tickets and churn ($r = +0.8723$) shows association; ticket volume reflects underlying service degradation.
   * **Selection Bias Awareness:** Acknowledging sample constraints before extrapolating findings to external populations.

---

## Objective 6: Practical Fundamentals Assignment Solutions

### 6.1 Assignment 1: Customer Churn Cohort EDA
Using the 20 customer cohort dataset (`customer_churn_analysis.csv`):
* **Cohort Size:** 20 subscribers
* **Overall Churn Rate:** **35.0%** (7 churned, 13 retained)
* **Average Tenure:** **18.4 months** (Median: 14.0 months)
* **Mean Monthly Charges:** **\$78.34** (Std Dev: \$26.81)
* **Total Cohort Sample Revenue:** **\$34,242.57**

#### Cohort Segmentation Comparison:
| Metric | Retained Cohort ($N=13$) | Churned Cohort ($N=7$) | Delta / Variance |
| :--- | :--- | :--- | :--- |
| **Average Tenure** | 26.1 months | 4.0 months | Retained cohort has **6.5x** higher tenure |
| **Mean Support Tickets** | 1.00 tickets | 4.29 tickets | Churned cohort had **4.3x** more complaints |
| **Mean Monthly Fee** | \$84.18 | \$67.50 | Retained customers hold higher tiers/contracts |

---

### 6.2 Assignment 2: Bivariate Correlation Analysis

```
Pearson Correlation Matrix with Churn Target:
-------------------------------------------------------
Tenure vs Churn:              r = -0.7027 (Strong Negative)
Support Tickets vs Churn:     r = +0.8723 (Very Strong Positive)
Satisfaction Tier vs Churn:   r = -0.7969 (Strong Negative)
Monthly Charges vs Churn:     r = -0.3046 (Moderate Negative)
Tenure vs Total Revenue:      r = +0.9786 (Near-Perfect Positive)
```

**Key Takeaways:**
* **Support Tickets ($r = +0.8723$)** is the single strongest indicator of customer attrition. Customers lodging 3 or more tickets represent immediate churn risks.
* **Tenure ($r = -0.7027$)** and **Satisfaction Tier ($r = -0.7969$)** serve as protective factors: subscribers who survive past 12 months with High/Very High satisfaction exhibit almost zero churn.

---

### 6.3 Assignment 3: Feedback Notes Text Mining
Extracting substantive keywords across customer reviews revealed critical operational drivers:
* **"speed"** (3 mentions) — broadband velocity concerns
* **"hours"** (2 mentions) — peak-hour latency and technician arrival delays
* **"technician"** (2 mentions) — field support responsiveness
* **"outages"** & **"throttling"** — critical triggers that prompted month-1 churn

---

### 6.4 Assignment 4: Hierarchical JSON E-Commerce Aggregation
Ingestion and parsing of multi-tier JSON order records (`ecommerce_orders.json`):
* **Processed Orders:** 4 orders across Austin, Seattle, Boston
* **Total Net Realized Revenue:** **\$1,730.64**
* **Volume by Category:**
  * `Accessories`: 7 units sold (\$178.65 net revenue)
  * `Electronics`: 3 units sold (\$1,398.99 net revenue)
  * `Audio`: 1 unit sold (\$153.00 net revenue)
* **Geographical Distribution:** Austin (50%), Seattle (25%), Boston (25%)

---

## Verification & Test Results

The assessment test harness (`src/test_fundamentals.py`) was executed with the following results:
```
[*] Running Test Suite: Data Science Fundamentals...
  [PASS] Test Mean: Passed
  [PASS] Test Median: Passed
  [PASS] Test Mode: Passed
  [PASS] Test Variance & Std Dev: Passed
  [PASS] Test Percentiles & IQR: Passed
  [PASS] Test Outlier Detection: Passed
  [PASS] Test Pearson Correlation: Passed
  [PASS] Test Bayes' Theorem: Passed
  [PASS] Test Schema Parsing: Passed

==========================================
 ALL 9 UNIT TESTS PASSED SUCCESSFULLY!
==========================================
```

All 6 objectives defined in the assessment specification have been completed and verified.
