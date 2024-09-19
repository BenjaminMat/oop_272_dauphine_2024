"""
Table of contents :
        ## Polymorphism in OOP
        ## Abstract class
        ## Protocol class
        ## Error handling
"""

from datetime import datetime
from scipy.stats import norm
import math

"""
## 1.10 - Polymorphism

    ** Definition/Concept **    

    ** Why to use it** 
       
    ** When to use it **
        
"""

class Asset:
    def price(self):
        pass

class Equity(Asset):
    def __init__(self, spot_price):
        self.spot_price = spot_price

    def price(self):
        return self.spot_price

class Option(Asset):
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        self.spot: float = spot
        self.strike: float = strike
        self.risk_free: float = risk_free
        self.ttm: float = time_to_maturity
        self.vol: float = volatility

    def compute_d1(self):
        d1 = (math.log(self.spot / self.strike) + (self.risk_free + 0.5 * self.vol ** 2) * self.ttm) / \
             (self.vol * math.sqrt(self.ttm))
        return d1

    def compute_d2(self):
        d2 = self.compute_d1() - self.vol * math.sqrt(self.ttm)
        return d2

class Call(Option):
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        super().__init__(spot, strike, risk_free, time_to_maturity, volatility)

    def price(self):
        n_d1 = norm.cdf(self.compute_d1())
        n_d2 = norm.cdf(self.compute_d2())
        return self.spot * n_d1 - self.strike * math.exp(-self.risk_free * self.ttm) * n_d2

class Put(Option):
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        super().__init__(spot, strike, risk_free, time_to_maturity, volatility)

    def price(self):
        n_minus_d1 = norm.cdf(-self.compute_d1())
        n_minus_d2 = norm.cdf(-self.compute_d2())
        return self.strike * math.exp(-self.risk_free * self.ttm) * n_minus_d2 - self.spot * n_minus_d1


def print_asset_price(asset: Asset):
    if isinstance(asset, Asset):
        print(f"The price of the {asset.__class__.__name__} is: {asset.price():.2f}")

# Instantiate different assets
stock = Equity(spot_price=100)
call = Call(spot=100, strike=90, volatility=0.2, time_to_maturity=1, risk_free=0.05)
put = Put(spot=100, strike=90, volatility=0.2, time_to_maturity=1, risk_free=0.05)

# Use the same function to print prices of different asset types
print_asset_price(stock)   # Output: The price of the asset is: 100.00
print_asset_price(call)  # Output: The price of the asset is: 16.70
print_asset_price(put) # Output: The price of the asset is: 2.31


"""
Types of Polymorphism:
         Runtime Polymorphism (Dynamic):
            Achieved through method overriding
            Resolved at runtime
            
        Compile-time Polymorphism (Static):
            Achieved through method overloading
            Resolved at compile time

Method Overriding: 
    
Method Overloading: 
    
"""

from multipledispatch import dispatch

class CalculatorDispatchExample:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(float, float)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

calc = CalculatorDispatchExample()
print(f"Sum of integers: {calc.add(5, 10)}")      # Output: 15
print(f"Sum of integers: {calc.add(5, 10, 15)}")  # Output: 30


class Calculator:
    def add(self, *args):
        if len(args) == 2:
            # Adds two numbers
            return args[0] + args[1]
        elif len(args) == 3:
            # Adds three numbers
            return args[0] + args[1] + args[2]
        else:
            raise ValueError("Invalid number of arguments")

# Usage
calc = Calculator()
print(calc.add(5, 10))      # Output: 15
print(calc.add(5, 10, 15))  # Output: 30


# A more concrete example of method overloading
class FinancialAssetUtil:
    def calculate_return(*args, method='simple'):
        """
        Calculates financial returns based on the inputs provided.

        Parameters:
        - If two numerical arguments are provided:
          - Calculates simple or logarithmic return between two values.
          - Use method='simple' (default) for simple return.
          - Use method='log' for logarithmic return.
        - If a list of prices is provided:
          - Calculates returns between consecutive prices.
          - Use method='simple' or method='log' to specify the return type.
        """
        if len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
            initial_value, final_value = args
            if method == 'simple':
                # Simple Return
                return (final_value - initial_value) / initial_value
            elif method == 'log':
                # Logarithmic Return
                return math.log(final_value / initial_value)
            else:
                raise ValueError("Invalid method. Use 'simple' or 'log'.")
        elif len(args) == 1 and isinstance(args[0], list):
            prices = args[0]
            if len(prices) < 2:
                raise ValueError("Price list must contain at least two prices.")
            returns = []
            for i in range(1, len(prices)):
                initial_value = prices[i - 1]
                final_value = prices[i]
                if method == 'simple':
                    ret = (final_value - initial_value) / initial_value
                elif method == 'log':
                    ret = math.log(final_value / initial_value)
                else:
                    raise ValueError("Invalid method. Use 'simple' or 'log'.")
                returns.append(ret)
            return returns
        else:
            raise ValueError("Invalid arguments provided.")

# Examples of usage:
# 1. Simple return between two values
initial_price = 100
final_price = 110
simple_return = FinancialAssetUtil.calculate_return(initial_price, final_price)
print(f"Simple Return: {simple_return:.2%}")  # Output: Simple Return: 10.00%

# 2. Logarithmic return between two values
log_return = FinancialAssetUtil.calculate_return(initial_price, final_price, method='log')
print(f"Logarithmic Return: {log_return:.4f}")  # Output: Logarithmic Return: 0.0953

# 3. Returns from a list of prices (simple returns)
price_series = [100, 105, 103, 108]
returns_simple = FinancialAssetUtil.calculate_return(price_series)
print(f"Simple Returns: {[f'{r:.2%}' for r in returns_simple]}")
# Output: Simple Returns: ['5.00%', '-1.90%', '4.85%']

# 4. Returns from a list of prices (logarithmic returns)
returns_log = FinancialAssetUtil.calculate_return(price_series, method='log')
print(f"Logarithmic Returns: {[f'{r:.4f}' for r in returns_log]}")
# Output: Logarithmic Returns: ['0.0488', '-0.0191', '0.0474']


"""
## Abstraction in Python

    ** Definition/Concept** 

    ** Why to use it** 

    ** When to use it  ** 

    ** How to implement an abstract class**
        You will find below a basic implementation of an abstract method. The AbstractClassExample is an abstract 
        class as it implements/ inherit the ABC class.
        When the @abstractmethod is defined prior a function, this makes this function mandatory for every subclass 
        implementing the abstract class. When @abstractmethod is not defined prior a function, its implementation 
        become non-mandatory. It considers as best practice to only implement mandatory method in an abstract class. 
"""

from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    @abstractmethod
    def mandatory_method(self):
        pass

    def not_mandatory_method(self):
        pass


class Subclass(AbstractClassExample):
    def mandatory_method(self):
        print("The subclass is implementing the mandatory method")

    def another_method(self):
        print("The subclass is implementing another method")


class AnotherSubclass(AbstractClassExample):
    def another_method(self):
        print("The subclass isn't implementing the mandatory method")


x = Subclass()
x.mandatory_method()
#y = AnotherSubclass() # TypeErrorWill: Can't instantiate abstract class AnotherSubclass
#z = AbstractClassExample() # TypeError: Can't instantiate abstract class


#TODO: Modify the Asset class above to make it an abstract class (code line 39 to 97)


"""
# Protocol in Python

    **Protocols**, introduced in Python 3.8, provide a way to define structural subtyping (often called “duck typing”).
     They allow you to define interfaces in a more flexible and Pythonic way compared to abstract base classes.

    ## Key Concepts
        - **Structural Subtyping**: An object is considered a subtype if it has the required methods and attributes, regardless of inheritance.
        - **No Runtime Enforcement**: Protocols are primarily used for static type checking and don’t enforce method implementation at runtime.
        - **Flexibility**: Classes don’t need to explicitly inherit from a Protocol to be considered compatible.

    To use Protocols, you need to import them from the `typing` module:

"""

from typing import Protocol

class Tradable(Protocol):
    symbol: str

    def current_price(self) -> float:
        ...

class Stock:
    def __init__(self, symbol: str, price_per_share: float):
        self.symbol = symbol
        self.price_per_share = price_per_share

    def current_price(self) -> float:
        return self.price_per_share

def display_instrument_price(instrument: Tradable):
    print(f"The current price of {instrument.symbol} is ${instrument.current_price():.2f}")

stock = Stock("AAPL", 150.0)
display_instrument_price(stock)  # Output: The current price of AAPL is $150.00

"""
Even though `Stock` doesn't inherit from `Tradable`, it is accepted by the `display_instrument_price` function
because it has the required `symbol` attribute and `current_price` method.
"""

#Another Example
class Pricable(Protocol):
    def price(self) -> float:
        ...

class StockPricable:
    def __init__(self, symbol: str, price_per_share: float):
        self.symbol = symbol
        self.price_per_share = price_per_share

    def price(self) -> float:
        return self.price_per_share


class CallPricable:
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        self.spot: float = spot
        self.strike: float = strike
        self.risk_free: float = risk_free
        self.ttm: float = time_to_maturity
        self.vol: float = volatility

    def compute_d1(self):
        d1 = (math.log(self.spot / self.strike) + (self.risk_free + 0.5 * self.vol ** 2) * self.ttm) / \
             (self.vol * math.sqrt(self.ttm))
        return d1

    def compute_d2(self):
        d2 = self.compute_d1() - self.vol * math.sqrt(self.ttm)
        return d2

    def price(self):
        n_d1 = norm.cdf(self.compute_d1())
        n_d2 = norm.cdf(self.compute_d2())
        return self.spot * n_d1 - self.strike * math.exp(-self.risk_free * self.ttm) * n_d2



def calculate_asset_list_value(assets: list[Pricable]) -> float:
    total = 0.0
    for asset in assets:
        total += asset.price()
    return total

# Create financial instruments
stock = StockPricable("AAPL", 150.0)
option = CallPricable(spot=100, strike=90, volatility=0.2, time_to_maturity=1, risk_free=0.05)

# Create a portfolio
asset_list = [stock, option]

# Calculate total value
total_value = calculate_asset_list_value(asset_list)
print(f"Total Portfolio Value: ${total_value:.2f}")

"""
## List comprehension

**Definition/Concept**

**Why to use it**

**When to use it**

"""

"""
Example : simple transformation using list comprehension
"""

import math
from datetime import datetime, timedelta

prices = [100.5, 102.3, 98.7, 105.6]

log_returns_with_for_loop = []
for i in range(1, len(prices)):
    log_return = math.log(prices[i] / prices[i - 1])
    log_returns_with_for_loop.append(log_return)

log_returns = [math.log(prices[i] / prices[i - 1]) for i in range(1, len(prices))]

print('same output for log_returns: ' + str(log_returns == log_returns_with_for_loop))

"""
Example : filtering  using list comprehension
"""
daily_returns = {datetime.today() - timedelta(days=5): 0.02,
                 datetime.today() - timedelta(days=4): -0.01,
                 datetime.today() - timedelta(days=3): 0.03,
                 datetime.today() - timedelta(days=2): -0.015,
                 datetime.today() - timedelta(days=1): 0.04}

profitable_days_with_for_loop = []
non_profitable_days_with_for_loop = []
for k, v in daily_returns.items():
    if v > 0:
        profitable_days_with_for_loop.append((k, v))
    elif v < 0:
        non_profitable_days_with_for_loop.append((k, v))

profitable_days = [(k, v) for k, v in daily_returns.items() if v > 0]  # filtering example
non_profitable_days = [(k, v) for k, v in daily_returns.items() if v < 0]  # filtering example

print('same output for profitable_days: ' + str(profitable_days == profitable_days_with_for_loop))
print('same output for non_profitable_days: ' + str(non_profitable_days == non_profitable_days_with_for_loop))

"""
Example : flattening using list comprehension
"""

list_of_list = [
    [1, 0.5, 0.3],
    [0.5, 1, 0.4],
    [0.3, 0.4, 1]
]

flat_list_with_for_loop = []
for sublist in list_of_list:
    for item in sublist:
        flat_list_with_for_loop.append(item)

flat_list = [item for sublist in list_of_list for item in sublist]

print('same output for flat_list: ' + str(flat_list == flat_list_with_for_loop))





"""
 ## Error Handling

**Python Exception Handling**
Exception Handling in Python: try, except, finally

 ** In-Depth Definition/Concept**

 ** Why use it **

** When to use it  **

"""


def divide(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("You tried to divide by zero.")
        division = None
    finally:
        return division




result = divide(10.5, 2.0)
print(result)
result1 = divide(10.5, 0.0)
print(result1)

"""
## custom exception
    ** Definition/Concept** 
       
    ** Why to use Custom Exceptions** 
       
    ** When to use Custom Exceptions  ** 
    
"""

"""
Example: Exception when particular behavior happened during execution, application to Updating quote for the
FinancialAsset object
"""


class NegativePriceException(Exception):
    """ Raised when the price of a financial asset is negative """
    pass


class QuoteCustomExceptionExample:
    def __init__(self, date: datetime, price: float):
        self.date = date
        self.price = price

    def __repr__(self):
        return f"Quote(date={self.date!r}, price={self.price!r})"


class FinancialAssetCustomExceptionExample:
    def __init__(self, ticker, quote, currency):
        self.ticker: str = ticker
        self.last_quote: QuoteCustomExceptionExample = quote
        self.currency: str = currency
        self.history: [QuoteCustomExceptionExample] = []

    def update_last_quote(self, new_quote: QuoteCustomExceptionExample):
        try:
            self.check_quote_for_asset(new_quote)
            self.history.append(self.last_quote)
            self.last_quote = new_quote
        except NegativePriceException as price_exception:
            print(str(price_exception))
            print("Quote has not been updated")

    def check_quote_for_asset(self, new_quote: QuoteCustomExceptionExample):
        if new_quote.price < 0:
            raise NegativePriceException(f"quote: {repr(new_quote)} for updating asset {self.ticker} is negative.")


last_date, last_close = datetime.today(), -175.0
equity_last_quote1 = QuoteCustomExceptionExample(last_date, last_close)
equity = FinancialAssetCustomExceptionExample('AAPL', equity_last_quote1, 'USD')
equity.update_last_quote(equity_last_quote1)

