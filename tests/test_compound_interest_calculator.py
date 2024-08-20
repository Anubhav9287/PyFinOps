import unittest
from pyfinops.compound_interest_calculator import CompoundInterestCalculator


class TestCompoundInterestCalculator(unittest.TestCase):
    def test_calculate_future_value(self):
        calculator = CompoundInterestCalculator(principal=1000, annual_rate=5, times_compounded=12, years=10)
        self.assertAlmostEqual(float(calculator.calculate_future_value()), 1647.01, places=2)


if __name__ == "__main__":
    unittest.main()
