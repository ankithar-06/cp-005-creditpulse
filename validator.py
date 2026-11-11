
def validate_inputs(
    payment,
    utilisation,
    account_age,
    enquiries,
    credit_types
):
    errors = []

    # 1. Validate on-time payment percentage
    if not isinstance(payment, (int, float)) or isinstance(payment, bool):
        errors.append("Payment percentage must be a number.")
    elif not 0 <= payment <= 100:
        errors.append("Payment percentage must be between 0 and 100.")

    # 2. Validate credit utilisation
    if not isinstance(utilisation, (int, float)) or isinstance(utilisation, bool):
        errors.append("Credit utilisation must be a number.")
    elif not 0 <= utilisation <= 100:
        errors.append("Credit utilisation must be between 0 and 100.")

    # 3. Validate oldest account age
    if not isinstance(account_age, (int, float)) or isinstance(account_age, bool):
        errors.append("Account age must be a number.")
    elif account_age < 0:
        errors.append("Account age cannot be negative.")

    # 4. Validate recent loan enquiries
    if not isinstance(enquiries, int) or isinstance(enquiries, bool):
        errors.append("Loan enquiries must be a whole number.")
    elif enquiries < 0:
        errors.append("Loan enquiries cannot be negative.")

    # 5. Validate number of credit types
    if not isinstance(credit_types, int) or isinstance(credit_types, bool):
        errors.append("Number of credit types must be a whole number.")
    elif credit_types < 0:
        errors.append("Number of credit types cannot be negative.")

    return errors


# Test the validation function independently
if __name__ == "__main__":

    print("CREDITPULSE - INPUT VALIDATION TEST")
    print("-" * 40)

    # Valid input test
    valid_result = validate_inputs(90, 30, 5, 2, 3)

    print("\nValid Input Test:")
    print(valid_result)

    # Invalid input test
    invalid_result = validate_inputs(120, -10, 5, -2, 3)

    print("\nInvalid Input Test:")
    for error in invalid_result:
        print("-", error)
