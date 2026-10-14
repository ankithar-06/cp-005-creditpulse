##  CreditPulse — Explainable Credit Score Estimation Engine

**Project ID:** CP-005  
**Level:** Intermediate  
**Domain:** Banking and FinTech

## 1. Overview

CreditPulse is an explainable credit score estimation tool designed to help young earners understand the factors that may influence their creditworthiness.

Many people struggle to understand why their loan applications are rejected or how their financial habits affect their credit profile. CreditPulse addresses this problem by estimating a score using a transparent, weighted scoring model and explaining which factors have the greatest negative impact.

Users can explore how changing their credit utilisation may improve their estimated score and receive actionable suggestions to build healthier credit habits.

> **Important:** CreditPulse is an educational prototype. Its estimated score is not an official credit score, does not replace scores issued by authorised credit bureaus, and cannot guarantee loan approval.

## 2. Problem Statement

Young earners often have limited knowledge of credit management. They may not understand the impact of late payments, high credit utilisation, recent loan enquiries, or a short credit history.

Traditional credit scoring systems may not provide users with a simple explanation of the factors influencing their scores.

CreditPulse aims to make credit score estimation more transparent, understandable, and interactive.

## 3. Objectives

- Estimate a credit score between 300 and 900.
- Use fixed, documented weights for transparent calculations.
- Classify estimated scores into Poor, Fair, Good, or Excellent.
- Identify the two factors contributing most negatively to the estimated score.
- Simulate the effect of reducing credit utilisation.
- Help users understand and improve their credit habits.

## 4. Core Features

All five compulsory features are included in the project scope.

### Feature 1: User Input

The system collects the following information:

| Input | Description |
|---|---|
| On-time payment percentage | Percentage of payments made on time |
| Credit utilisation | Percentage of available credit currently used |
| Age of oldest account | Age of the user's oldest credit account in years |
| Recent loan enquiries | Number of recent credit enquiries |
| Number of credit types | Number of different credit categories held |

### Feature 2: Weighted Credit Score Calculation

CreditPulse uses a fixed, documented weighted scoring model.

| Factor | Weight |
|---|---:|
| On-time payment percentage | 35% |
| Credit utilisation | 30% |
| Age of oldest account | 15% |
| Recent loan enquiries | 10% |
| Number of credit types | 10% |
| **Total** | **100%** |

Each input is converted into a normalised factor score between 0 and 100. The weighted average is then mapped to the target score range of 300–900.

**Formula:**

`Weighted Score = Σ (Normalised Factor Score × Factor Weight)`

`Estimated Credit Score = 300 + (Weighted Score × 6)`

The final score is rounded to the nearest integer and constrained to the range of 300–900.

The normalisation rules for each factor must be documented in the implementation so the calculation remains reproducible and explainable.

### Feature 3: Score Classification

CreditPulse groups estimated scores into four categories.

| Estimated Score | Classification |
|---|---|
| 300–499 | Poor |
| 500–649 | Fair |
| 650–749 | Good |
| 750–900 | Excellent |

These thresholds are illustrative categories for this project, not official credit bureau classifications.

### Feature 4: Explainable Results

After calculating the estimated score, the application identifies the two weakest contributing factors.

Example explanations:

- **Payment history:** A low on-time payment percentage reduces the payment-history contribution.
- **Credit utilisation:** Using a high percentage of available credit reduces the utilisation contribution.
- **Credit history:** A relatively young oldest account receives a lower history score.
- **Recent enquiries:** Multiple recent loan enquiries reduce the enquiry contribution.
- **Credit mix:** A limited variety of credit types may reduce the credit-mix contribution under this model.

Explanations are generated from the same factor scores and weights used in the calculation.

### Feature 5: What-If Credit Utilisation Simulator

Users can enter a target credit utilisation percentage to see how their estimated score might change.

**Example workflow:**

1. Enter the current financial inputs.
2. Calculate the estimated credit score.
3. Enter a lower target utilisation percentage.
4. Recalculate the score using the new utilisation value.
5. Display the original score, simulated score, and score difference.

`Score Change = Simulated Score − Original Score`

The simulation changes only the utilisation input. All other inputs and scoring weights remain constant.

## 5. Optional Stretch Features

### Monthly Score Tracking

- Store estimated scores with their calculation dates.
- Display historical scores in a line chart.
- Help users monitor changes over time.

### Personalised Improvement Plan

Generate short suggestions based on the weakest factors, such as:

- Pay bills and EMIs on time.
- Reduce outstanding balances relative to available credit.
- Avoid unnecessary loan applications.
- Maintain older credit accounts responsibly.
- Manage existing credit products carefully.

Recommendations should be educational and should not encourage users to borrow unnecessarily.

## 6. Technology Stack

The technology stack can be adapted to the implementation.

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python
- **Scoring engine:** Python functions implementing the weighted model
- **Data visualisation:** Matplotlib or Chart.js
- **Data storage (optional):** SQLite
- **Version control:** Git and GitHub

A simple prototype can also be built entirely in Python using Streamlit.

## 7. System Workflow

1. The user opens the CreditPulse application.
2. The user enters the five required credit-related inputs.
3. The application validates the inputs.
4. Each factor is normalised according to documented rules.
5. The weighted scoring engine calculates the estimated score.
6. The score is classified into one of four categories.
7. The two weakest factors and their explanations are displayed.
8. The user enters a target credit utilisation percentage.
9. The application calculates and displays the simulated score.
10. Optional features provide a score history and improvement suggestions.

## 8. Project Structure

A suggested project directory is:

```text
CreditPulse/
├── app.py
├── scoring.py
├── explanations.py
├── simulator.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_scoring.py
├── data/
│   └── .gitkeep
└── assets/
    └── style.css
```

**File responsibilities:**

- `app.py` — User interface and application workflow.
- `scoring.py` — Input normalisation, weighted score calculation, and classification.
- `explanations.py` — Identification and explanation of the two weakest factors.
- `simulator.py` — What-if credit utilisation calculations.
- `requirements.txt` — Python dependencies.
- `tests/test_scoring.py` — Unit tests for scoring rules and edge cases.
- `assets/style.css` — Styling for a web-based interface.

The structure is a suggested starting point and can be adjusted to match the final implementation.

## 9. Installation and Execution

### Prerequisites

- Python 3.10 or later
- Git
- A code editor such as Visual Studio Code

### Setup

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CreditPulse
```

Create and activate a virtual environment on Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application according to the selected framework.

For a Streamlit implementation:

```bash
streamlit run app.py
```

For a Flask implementation, use the corresponding Flask run command.

**Note:** These commands assume the corresponding files and framework have been implemented.

## 10. Input Validation and Testing

The application should validate the following conditions:

- On-time payment percentage must be between 0 and 100.
- Credit utilisation must be between 0 and 100.
- Account age must not be negative.
- Recent loan enquiries must be a non-negative integer.
- Number of credit types must be a non-negative integer.
- Target utilisation must be between 0 and 100.
- The calculated score must always remain between 300 and 900.
- Invalid inputs must produce understandable error messages.

Unit tests should verify score boundaries, category thresholds, factor normalisation, explanation ranking, and what-if simulation behaviour.

## 11. Privacy and Responsible Use

CreditPulse should collect only the information necessary for estimation.

- Do not request banking passwords, card PINs, or OTPs.
- Do not collect actual credit bureau reports without appropriate authorisation.
- Protect any stored user information.
- Clearly distinguish estimated results from official credit scores.
- Avoid presenting the estimate as a loan approval prediction.

The weighted model is a simplified educational model and does not represent the proprietary methodology of any credit bureau or lender.

## 12. Expected Outcome

CreditPulse provides an understandable estimated credit score, identifies the two factors with the greatest negative impact, and demonstrates how changing credit utilisation affects the result.

The project demonstrates practical applications of weighted scoring models, input validation, explainable calculations, and what-if simulation in financial technology.

## 13. Future Enhancements

- Add interactive dashboards and historical trend charts.
- Introduce downloadable score reports.
- Add user accounts with secure data storage.
- Improve explanations with personalised recommendations.
- Evaluate the model against appropriately sourced, authorised datasets.
- Explore machine learning models while retaining transparent explanations.

## 14. Interview Talking Points

**Weighted scoring model:** Explain how normalisation and fixed weights combine multiple inputs into a single score.

**Explainability:** Describe how the system ranks factor contributions and generates understandable reasons for a result.

**What-if simulation:** Explain how the system changes one input while keeping the other inputs constant to calculate a new score.

**Validation:** Discuss boundary checks, error handling, reproducibility, and unit tests.

**Responsible FinTech design:** Explain why the result is labelled an estimate rather than an official credit score.

---

**Project:** CreditPulse — Explainable Credit Score Estimation Engine  
**Project ID:** CP-005  
**Level:** Intermediate  
**Domain:** Banking and FinTech