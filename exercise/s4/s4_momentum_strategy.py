"""
You need to implement a portfolio for a Momentum strategy.
The momentum strategy is computed by subtracting the average price from the lookback_period from the current price.
Signal generated:
Buy Signal (1): If momentum is positive.
Sell Signal (-1): If momentum is negative.

The Portfolio class, should generate the momentum signal, sell all the position with a sell signal and equal weight all
the position with a buy signal.

TASK:
    - Create a MomentumStrategy class that inherits from Strategy.
    - Implement the generate_signals method to produce buy or sell signals based on the momentum of asset prices on a defined lookback_period.
    - Use the Instrument and Position classes to manage our assets and their price histories.

**Tips**:
- Use the methods and attributes of other provided classes in S4_resources.
- Before starting the exercise be sure to fully understand how the object provided for it worked.

"""