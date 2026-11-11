# Data Science Fundamentals Assessment

This is a Python-based project I made to practise and understand some basic concepts of Data Science. It covers statistical calculations, data analysis, and working with different types of data.

The main aim of this project was to apply the concepts practically instead of just learning them theoretically.

## About the Project

The project includes different tasks related to statistics and data handling. It uses Python to perform calculations, analyse a customer dataset, process order details, and test the results.

## Features

Some of the main things covered in this project are:

- **Statistical Calculations:** Mean, median, mode, variance, and standard deviation.
- **Data Analysis:** Finding percentiles, IQR, and detecting outliers.
- **Correlation:** Using Pearson correlation to understand relationships between variables.
- **Bayes' Theorem:** Applying basic probability concepts.
- **Customer Churn Analysis:** Analysing customer records and calculating the churn percentage.
- **JSON Processing:** Reading order data and calculating total net revenue.
- **Schema Parsing:** Working with structured data.
- **Unit Testing:** Checking whether the different functions give the expected results.

## Technologies Used

- Python
- Jupyter Notebook
- CSV
- JSON

## Project Results

The project was tested successfully, and all 9 unit tests passed.

A few results from the assessment:

- Customer records analysed: 20
- Customer churn rate: 35%
- Orders processed: 4
- Net revenue calculated: $1,730.64
- All 6 assessment objectives passed.

## How to Run the Project

If you want to run this project on your computer:

1. Clone this repository or download the project.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python run.py
```

The program will execute the assessment tasks and display the results in the terminal.

## What I Learned

While working on this project, I got a better understanding of how Python can be used for basic data analysis and statistical operations. I also got some practical experience with CSV and JSON files, writing test cases, and organising a Python project.

This project helped me connect some of the concepts I had learned with actual implementation.

---

## Visual Studio Code Integration

This project is configured for VS Code with pre-configured settings, launch configurations, and build tasks in `.vscode/`:

1. **Workspace Location:**
   `C:\Users\User\.gemini\antigravity\scratch\data_science_fundamentals_assessment`
2. **Opening in VS Code from terminal:**
   ```bash
   code "C:\Users\User\.gemini\antigravity\scratch\data_science_fundamentals_assessment"
   ```
3. **Running inside VS Code:**
   * Press **F5** or go to the **Run & Debug** panel to select and run:
     * `1. Run Full Assessment`
     * `2. Run Unit Tests (9 Tests)`
     * `3. Run Unified Entrypoint (run.py)`
   * Press **Ctrl + Shift + B** to trigger the default build task (`Run Full Assessment Suite`).

---

## Repository Structure

```text
data_science_fundamentals_assessment/
├── .github/
│   └── workflows/
│       └── ci.yml                            # Multi-platform (Ubuntu, Windows) CI matrix
├── .vscode/
│   ├── launch.json                           # F5 debug configurations for VS Code
│   ├── settings.json                         # Workspace interpreter and environment setup
│   └── tasks.json                            # Ctrl+Shift+B one-click build and test tasks
├── data/
│   ├── customer_churn_analysis.csv           # Multi-attribute customer cohort dataset
│   └── ecommerce_orders.json                 # Hierarchical semi-structured JSON order logs
├── notebooks/
│   └── Data_Science_Fundamentals_Assessment.ipynb # Interactive Jupyter Notebook
├── reports/
│   ├── Data_Science_Fundamentals_Report.docx # Formatted Microsoft Word (.docx) report for submission
│   ├── Data_Science_Fundamentals_Report.doc  # Microsoft Word (.doc) formatted report
│   └── Data_Science_Fundamentals_Report.md   # Comprehensive theoretical & analytical markdown report
├── src/
│   ├── data_handler.py                       # Ingestion, validation, and schema classification
│   ├── fundamentals_assessment.py            # Master assessment runner covering all 6 objectives
│   ├── generate_docx_report.py               # Word .docx and .doc report generator
│   ├── statistical_toolkit.py                # Pure Python statistical algorithms
│   └── test_fundamentals.py                 # Self-contained unit test suite (9 test cases)
├── .gitignore                                # Standard Python and editor ignore rules
├── generate_notebook.py                      # Notebook generator utility
├── LICENSE                                   # MIT Open Source License
├── README.md                                 # Project documentation and guide
├── requirements.txt                          # Optional packages for interactive notebooks
├── run.py                                    # Unified cross-platform entry point
├── run_project.bat                           # Double-click Windows batch runner
└── run_project.ps1                           # One-click PowerShell runner
```

---

## Assessment Objectives & Coverage

### 1. Data Science Fundamentals & Problem Framing
* **The 7 Lifecycle Stages:** Problem Definition, Data Ingestion, Data Preparation, Exploratory Data Analysis (EDA), Feature Engineering & Modeling, Evaluation, Deployment & Monitoring.
* **The 4 Analytical Archetypes:** Descriptive, Diagnostic, Predictive, and Prescriptive analytics.
* **Industry Applications:** Real-world case studies in Telecom Churn, FinTech Fraud Detection, Healthcare Diagnostics, and E-commerce Personalization.

### 2. Python Programming Basics
* Primitives, types, operators, and control flow.
* Comprehensive collections review: mutable `list`, immutable `tuple`, unique `set`, and key-value `dict`.
* Defensive programming with exception handling (`try-except`), safe division, and comprehensions.

### 3. Statistical Foundations & Computations
* **Central Tendency:** Mean ($\bar{x}$), Median ($\tilde{x}$), Mode.
* **Measures of Dispersion:** Sample Variance ($s^2$ with Bessel's correction $n-1$), Population Variance ($\sigma^2$), Standard Deviation ($s$).
* **Quartiles & Outlier Detection:** $Q_1$, $Q_2$, $Q_3$, Interquartile Range ($IQR$), and Tukey Outlier Fences ($[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$).
* **Correlation:** Pearson's correlation coefficient ($r$).
* **Probability Theory:** Conditional probability and Bayes' Theorem.

### 4. Data Types & Structures in Real Analysis
* Numerical Continuous (`monthly_charges` -> scaling, standardization).
* Numerical Discrete (`support_tickets` -> Poisson/negative binomial modeling).
* Categorical Nominal (`contract_type` -> One-Hot encoding).
* Categorical Ordinal (`satisfaction_tier` -> Monotonic integer encoding).
* Temporal / Datetime (`signup_date` -> Day-of-week, quarter, tenure extraction).
* Text / Unstructured (`feedback_notes` -> Tokenization, keyword extraction, sentiment).

### 5. Data Science Best Practices
* Semantic, PEP 8-compliant variable naming (`customer_churn_rate` vs `cr`).
* Deterministic random seed management (`random.seed(42)`).
* Separation of concerns: modular ETL, computation, reporting, and notebooks.
* Awareness of ethical principles, selection bias, and **Correlation $\neq$ Causation**.

### 6. Practical Fundamentals Assignments
* **Assignment 1 (Customer Churn EDA):** Analyzed 20 subscriber records; revealed a 35.0% churn rate with retained customers having 6.5x longer tenure.
* **Assignment 2 (Bivariate Correlation):** Computed $r(\text{Support Tickets}, \text{Churn}) = +0.8723$ (strongest attrition driver) and $r(\text{Tenure}, \text{Churn}) = -0.7027$.
* **Assignment 3 (Feedback Text Mining):** Extracted critical service friction points: "speed", "outages", "technician".
* **Assignment 4 (Hierarchical JSON Aggregation):** Parsed multi-nested order logs totaling \$1,730.64 net revenue across 3 product categories.

---

## Verification & Test Results

```text
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

---
**Project:** Data Science Fundamentals Assessment  
**Language:** Python 3.10+
