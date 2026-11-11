
import unittest

from scoring import (
    calculate_factor_scores,
    calculate_credit_score,
    classify_score
)


class TestCreditPulseScoring(unittest.TestCase):

    def test_factor_scores(self):
        factors = calculate_factor_scores(95, 25, 6, 1, 3)

        self.assertEqual(factors["payment_history"], 95)
        self.assertEqual(factors["credit_utilisation"], 75)
        self.assertEqual(factors["account_age"], 60)
        self.assertEqual(factors["loan_enquiries"], 80)
        self.assertEqual(factors["credit_mix"], 60)

    def test_score_is_within_range(self):
        factors = calculate_factor_scores(95, 25, 6, 1, 3)
        score = calculate_credit_score(factors)

        self.assertGreaterEqual(score, 300)
        self.assertLessEqual(score, 900)

    def test_score_classification(self):
        self.assertEqual(classify_score(450), "Poor")
        self.assertEqual(classify_score(550), "Fair")
        self.assertEqual(classify_score(700), "Good")
        self.assertEqual(classify_score(800), "Excellent")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_factor_scores(120, 25, 6, 1, 3)


if __name__ == "__main__":
    unittest.main()
