
from validator import validate_inputs

# Fixed weights for each credit factor
WEIGHTS = {
    "payment_history": 0.35,
    "credit_utilisation": 0.30,
    "account_age": 0.15,
    "loan_enquiries": 0.10,
    "credit_mix": 0.10
}


def calculate_factor_scores(
    payment,
    utilisation,
    account_age,
    enquiries,
    credit_types
):
    """
    Convert user inputs into normalised factor scores (0-100).
    """

    errors = validate_inputs(
        payment,
        utilisation,
        account_age,
        enquiries,
        credit_types
    )

    if errors:
        raise ValueError("; ".join(errors))

    factor_scores = {
        "payment_history": float(payment),

        "credit_utilisation": max(
            0, 100 - utilisation
        ),

        "account_age": min(
            (account_age / 10) * 100, 100
        ),

        "loan_enquiries": max(
            0, 100 - (enquiries * 20)
        ),

        "credit_mix": min(
            (credit_types / 5) * 100, 100
        )
    }

    return factor_scores


def calculate_credit_score(factor_scores):
    """
    Calculate weighted score and map it to 300-900.
    """

    if set(factor_scores) != set(WEIGHTS):
        raise ValueError("All five credit factor scores are required.")

    for factor, value in factor_scores.items():
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError(f"{factor} must be numeric.")

        if not 0 <= value <= 100:
            raise ValueError(f"{factor} must be between 0 and 100.")

    weighted_score = sum(
        factor_scores[factor] * WEIGHTS[factor]
        for factor in WEIGHTS
    )

    final_score = round(300 + (weighted_score * 6))

    return max(300, min(900, final_score))


def classify_score(score):
    """
    Classify the estimated credit score.
    """

    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise ValueError("Score must be numeric.")

    if not 300 <= score <= 900:
        raise ValueError("Score must be between 300 and 900.")

    if score < 500:
        return "Poor"

    elif score < 650:
        return "Fair"

    elif score < 750:
        return "Good"

    else:
        return "Excellent"


# Independent testing
if __name__ == "__main__":

    print("=" * 45)
    print("       CREDITPULSE SCORING ENGINE")
    print("=" * 45)

    factors = calculate_factor_scores(
        payment=95,
        utilisation=25,
        account_age=6,
        enquiries=1,
        credit_types=3
    )

    score = calculate_credit_score(factors)
    category = classify_score(score)

    print("\nFactor Scores:")

    for factor, value in factors.items():
        print(f"{factor}: {value:.2f}")

    print("\nEstimated Credit Score:", score)
    print("Credit Category:", category)

    print("\nScoring engine executed successfully!")
