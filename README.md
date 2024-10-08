# PyFinOps

FinToolkit is a comprehensive Python package for various financial calculations and tools. It includes:

- **SIP Calculator**: Calculate the future value of Systematic Investment Plan (SIP) investments.
- **Compound Interest Calculator**: Calculate the future value of investments with compound interest.

## Installation

You can install PyFinOps via pip:

```bash
pip install PyFinOps
```

# How to use:
## SIP Calculator
Calculate the future value of a Systematic Investment Plan (SIP) investment.

```bash
from pyfinops import SIPCalculator

# Create an instance of the calculator
sip_calculator = SIPCalculator(monthly_investment=500, annual_rate=12, years=10)
# Calculate the future value of the SIP investment
future_value = sip_calculator.calculate_future_value()
print(f"Future Value of SIP: ${future_value}")
# Display SIP details including total investment and interest earned
sip_calculator.display_sip_details()
```

## Compound Interest Calculator
Calculate the future value of an investment using compound interest.

```bash
from pyfinops import CompoundInterestCalculator

# Create an instance of the calculator
compound_interest_calculator = CompoundInterestCalculator(principal=1000, annual_rate=5, times_compounded=12, years=10)

# Calculate the future value of the investment
future_value = compound_interest_calculator.calculate_future_value()
print(f"Future Value of Investment: ${future_value}")

# Display investment details including principal, future value, and total interest earned
compound_interest_calculator.display_investment_details()

```

## Command line usage

```
sip-calculator --monthly-investment 500 --annual-rate 12 --years 10

compound-interest --principal 1000 --annual-rate 5 --times-compounded 12 --years 10
