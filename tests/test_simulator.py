
import unittest

from simulator import simulate_utilisation


class TestCreditPulseSimulator(unittest.TestCase):

    def test_reducing_utilisation_improves_score(self):
        result = simulate_utilisation(
            payment=95,
            current_utilisation=70,
            account_age=6,
            enquiries=1,
            credit_types=3,
            new_utilisation=25
        )

        self.assertGreater(
            result["simulated_score"],
            result["original_score"]
        )

    def test_increasing_utilisation_reduces_score(self):
        result = simulate_utilisation(
            payment=95,
            current_utilisation=25,
            account_age=6,
            enquiries=1,
            credit_types=3,
            new_utilisation=70
        )

        self.assertLess(
            result["simulated_score"],
            result["original_score"]
        )

    def test_invalid_utilisation(self):
        with self.assertRaises(ValueError):
            simulate_utilisation(
                95, 25, 6, 1, 3, 120
            )


if __name__ == "__main__":
    unittest.main()
