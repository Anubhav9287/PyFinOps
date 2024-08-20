import unittest
from pyfinops.sip_calculator import SIPCalculator


class TestSIPCalculator(unittest.TestCase):
    def test_calculate_future_value(self):
        sip = SIPCalculator(monthly_investment=1000, annual_rate=12, years=10)
        self.assertAlmostEqual(float(sip.calculate_future_value()), 232339.08, places=2)


if __name__ == "__main__":
    unittest.main()
