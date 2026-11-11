
import unittest
from validator import validate_inputs


class TestCreditPulseValidator(unittest.TestCase):

    def test_valid_inputs(self):
        errors = validate_inputs(95, 25, 6, 1, 3)
        self.assertEqual(errors, [])

    def test_invalid_payment_percentage(self):
        errors = validate_inputs(120, 25, 6, 1, 3)
        self.assertTrue(len(errors) > 0)

    def test_invalid_utilisation(self):
        errors = validate_inputs(95, -10, 6, 1, 3)
        self.assertTrue(len(errors) > 0)

    def test_negative_account_age(self):
        errors = validate_inputs(95, 25, -2, 1, 3)
        self.assertTrue(len(errors) > 0)

    def test_negative_enquiries(self):
        errors = validate_inputs(95, 25, 6, -1, 3)
        self.assertTrue(len(errors) > 0)

    def test_negative_credit_types(self):
        errors = validate_inputs(95, 25, 6, 1, -2)
        self.assertTrue(len(errors) > 0)


if __name__ == "__main__":
    unittest.main()
