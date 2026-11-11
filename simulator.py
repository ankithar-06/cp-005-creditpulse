
from scoring import (
    calculate_factor_scores,
    calculate_credit_score,
    classify_score
)


def simulate_utilisation(
    payment,
    current_utilisation,
    account_age,
    enquiries,
    credit_types,
    new_utilisation
):
    """
    Simulate credit score after changing utilisation.

    All other financial inputs remain unchanged.
    """

    # Calculate original factor scores
    original_factors = calculate_factor_scores(
        payment,
        current_utilisation,
        account_age,
        enquiries,
        credit_types
    )

    # Calculate original credit score
    original_score = calculate_credit_score(
        original_factors
    )

    # Calculate new factor scores
    simulated_factors = calculate_factor_scores(
        payment,
        new_utilisation,
        account_age,
        enquiries,
        credit_types
    )

    # Calculate simulated score
    simulated_score = calculate_credit_score(
        simulated_factors
    )

    score_change = simulated_score - original_score

    return {
        "original_score": original_score,
        "simulated_score": simulated_score,
        "original_category": classify_score(original_score),
        "simulated_category": classify_score(simulated_score),
        "score_change": score_change,
        "current_utilisation": current_utilisation,
        "new_utilisation": new_utilisation
    }


# Independent testing
if __name__ == "__main__":

    print("=" * 45)
    print("     CREDITPULSE WHAT-IF SIMULATOR")
    print("=" * 45)

    result = simulate_utilisation(
        payment=95,
        current_utilisation=70,
        account_age=6,
        enquiries=1,
        credit_types=3,
        new_utilisation=25
    )

    print("\nCURRENT CREDIT PROFILE")
    print("Utilisation:", result["current_utilisation"], "%")
    print("Estimated Score:", result["original_score"])
    print("Classification:", result["original_category"])

    print("\nSIMULATED CREDIT PROFILE")
    print("New Utilisation:", result["new_utilisation"], "%")
    print("Estimated Score:", result["simulated_score"])
    print("Classification:", result["simulated_category"])

    print("\nSCORE DIFFERENCE:", result["score_change"])

    print("\nSimulation executed successfully!")
