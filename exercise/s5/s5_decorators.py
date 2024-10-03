"""
Exercise: Performance Measurement and Memoization with Decorators

Part 1: Create a decorator named @timing_decorator that measures the execution time of a function and prints the elapsed
time when the function completes.

Steps:
Define a decorator timing_decorator that:
    Accepts a function as input.
    Uses time from the time module to measure the execution time.
    Prints out the function’s name and how long it took to execute.
    Apply this decorator to a function that calculates the Black-Scholes option price for European options.

Hint:
For timing the execution of your code use the time package. To start and end the timer you can use the
following line :
start_time = time.time()
end_time = time.time()
The execution time is the difference between the two.
"""
import math
import time

from scipy.stats import norm

#TODO: implement the decorator here:


"""
Part 2: Creating the validate_inputs Decorator

Define a decorator validate_inputs that:
    Checks if the inputs to a function are valid.
    For any invalid input, raises a ValueError.
    The decorator should specifically check for the following conditions:
        Prices must be positive.
        Time to maturity (T) must be greater than 0.
        Volatility must be a float between 0 and 1.
        Apply this decorator to relevant method to ensure inputs are valid before the calculation proceeds.
"""

#TODO: implement the decorator here:


"""
Create a decorator named @MemoizationDecorator to cache the results of functions for given inputs to avoid redundant 
calculations.

Steps:
Define a decorator memoization_decorator that:
    Caches the function’s results using a dictionary where the name of the function arguments are the keys
    If the function has already been called with a particular set of arguments, the decorator should return 
    the cached result instead of recalculating it.
    Apply this decorator to the option classes when you think it make sense to do it.

Create test cases where the function is called multiple times with the same and different arguments. 
Observe the time taken with and without memoization using your timing_decorator from Part 1.
"""

#TODO: implement the decorator here:

class Option:
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        self.spot: float = spot
        self.strike: float = strike
        self.risk_free: float = risk_free
        self.ttm: float = time_to_maturity
        self.vol: float = volatility

    @MemoizationDecorator()
    def compute_d1(self):
        d1 = (math.log(self.spot / self.strike) + (self.risk_free + 0.5 * self.vol ** 2) * self.ttm) / \
             (self.vol * math.sqrt(self.ttm))
        return d1

    @MemoizationDecorator()
    def compute_d2(self):
        d2 = self.compute_d1() - self.vol * math.sqrt(self.ttm)
        return d2

    def compute_vega(self):
        return self.spot * norm.pdf(self.compute_d1()) * math.sqrt(self.ttm)


class Call(Option):
    @timing_decorator
    def compute_price(self):
        n_d1 = norm.cdf(self.compute_d1())
        n_d2 = norm.cdf(self.compute_d2())
        return self.spot * n_d1 - self.strike * math.exp(-self.risk_free * self.ttm) * n_d2

    def compute_delta(self):
        return norm.cdf(self.compute_d1())

    def compute_rho(self):
        return self.strike * self.ttm * math.exp(-self.risk_free * self.ttm) * norm.cdf(self.compute_d2())

    def compute_theta(self):
        return (-self.spot * self.vol * norm.pdf(self.compute_d1()) / (2 * math.sqrt(self.ttm))) \
               - self.risk_free * self.strike * math.exp(-self.risk_free * self.ttm) * norm.cdf(self.compute_d2())


class Put(Option):
    @timing_decorator
    def compute_price(self):
        n_minus_d1 = norm.cdf(-self.compute_d1())
        n_minus_d2 = norm.cdf(-self.compute_d2())
        return self.strike * math.exp(-self.risk_free * self.ttm) * n_minus_d2 - self.spot * n_minus_d1

    def compute_delta(self):
        return norm.cdf(self.compute_d1()) - 1

    def compute_rho(self):
        return -self.strike * self.ttm * math.exp(-self.risk_free * self.ttm) * norm.cdf(-self.compute_d2())

    def compute_theta(self):
        return (-self.spot * self.vol * norm.pdf(self.compute_d1()) / (2 * math.sqrt(self.ttm))) \
               + self.risk_free * self.strike * math.exp(-self.risk_free * self.ttm) * norm.cdf(-self.compute_d2())



if __name__ == '__main__':
    call = Call(spot=200, strike=250, risk_free=0.05, time_to_maturity=1, volatility=0.15)
    print(f'call price {round(call.compute_price(), 4)}')
