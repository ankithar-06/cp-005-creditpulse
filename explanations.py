
from scoring import WEIGHTS


FACTOR_NAMES = {
    "payment_history": "Payment History",
    "credit_utilisation": "Credit Utilisation",
    "account_age": "Credit History Age",
    "loan_enquiries": "Recent Loan Enquiries",
    "credit_mix": "Credit Mix"
}


def generate_explanation(factor_scores):
    """
    Identify the two factors contributing the largest
    weighted deductions from the maximum possible score.
    """

    if set(factor_scores) != set(WEIGHTS):
        raise ValueError("All five factor scores are required.")

    for factor, value in factor_scores.items():
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError(f"{factor} must be numeric.")

        if not 0 <= value <= 100:
            raise ValueError(f"{factor} must be between 0 and 100.")

    deductions = {}

    for factor, score in factor_scores.items():
        deductions[factor] = (100 - score) * WEIGHTS[factor]

    weakest_factors = sorted(
        deductions,
        key=lambda factor: deductions[factor],
        reverse=True
    )[:2]

    explanations = []

    for factor in weakest_factors:

        score = factor_scores[factor]

        if factor == "payment_history":
            message = (
                "Your on-time payment percentage is low. "
                "Try paying bills and EMIs before their due dates."
            )

        elif factor == "credit_utilisation":
            message = (
                "Your credit utilisation is high. "
                "Try reducing outstanding balances relative "
                "to your available credit."
            )

        elif factor == "account_age":
            message = (
                "Your oldest credit account has a relatively "
                "short history. Build a consistent credit history "
                "over time."
            )

        elif factor == "loan_enquiries":
            message = (
                "Recent loan enquiries are affecting your score. "
                "Avoid unnecessary credit applications."
            )

        else:
            message = (
                "Your credit mix contribution is relatively low. "
                "Manage existing credit responsibly rather than "
                "taking new loans just to increase credit variety."
            )

        explanations.append({
            "factor": FACTOR_NAMES[factor],
            "factor_score": round(score, 2),
            "weighted_deduction": round(deductions[factor], 2),
            "explanation": message
        })

    return explanations


# Independent testing
if __name__ == "__main__":

    print("=" * 45)
    print("    CREDITPULSE EXPLANATION ENGINE")
    print("=" * 45)

    sample_scores = {
        "payment_history": 95,
        "credit_utilisation": 75,
        "account_age": 60,
        "loan_enquiries": 80,
        "credit_mix": 60
    }

    results = generate_explanation(sample_scores)

    print("\nTop 2 Factors Pulling Your Score Down:\n")

    for index, result in enumerate(results, start=1):

        print(f"{index}. {result['factor']}")
        print(f"   Factor Score: {result['factor_score']}")
        print(f"   Weighted Deduction: {result['weighted_deduction']}")
        print(f"   Explanation: {result['explanation']}")
        print()

    print("Explanation engine executed successfully!")
