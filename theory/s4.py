"""
Table of contents :
    ## Python Exception Handling
    ## Custom Exception
    ## Utility classes
    ## Static Methods
    ## Data class
    ## Decorators
    ## Built-in Decorator
    ## Class-based Decorator



"""
from datetime import datetime

"""
## Python Exception Handling

    Exception Handling in Python: try, except, finally
     ** In-Depth Definition/Concept**
   
    ** Why use it **
        
    ** When to use it  **
        
"""

def divide(a, b):
    division = None
    try:
        division = a / b
    except ZeroDivisionError:
        print("You tried to divide by zero.")
    finally:
        return division

result = divide(10.5, 2.0)
print(result)
result1 = divide(10.5, 0.0)
print(result1)


"""
## Custom Exception
    ** Definition/Concept** 
        
    ** Why to use Custom Exceptions** 
        - **Understandability**:  
        - **Control flow**: 
        - **Modularity**: 
        
    ** When to use Custom Exceptions  ** 

"""

"""
Example: Exception when particular behavior happened during execution, application to Updating quote for the
FinancialAsset object
"""

class NegativePriceException(Exception):
    """ Raised when the price of a financial asset is negative """
    pass


class Quote:
    def __init__(self, date: datetime, price: float):
        self.date = date
        self.price = price

    def __repr__(self):
        return f"Quote(date={self.date!r}, price={self.price!r})"


class FinancialAsset:
    def __init__(self, ticker, quote, currency):
        self.ticker: str = ticker
        self.last_quote: Quote = quote
        self.currency: str = currency
        self.history: [Quote] = []

    def update_last_quote(self, new_quote: Quote):
        try:
            self.__check_quote_for_asset(new_quote)
            self.history.append(self.last_quote)
            self.last_quote = new_quote
        except NegativePriceException as price_exception:
            print(str(price_exception))
            print("Quote has not been updated")
            #raise
        finally:
            pass

    def __check_quote_for_asset(self, new_quote: Quote):
        if new_quote.price < 0:
            raise NegativePriceException(f"quote: {repr(new_quote)} for updating asset {self.ticker} is negative.")


last_date, last_close = datetime.now(), 175.0
equity_last_quote = Quote(last_date, last_close)
equity = FinancialAsset('AAPL', equity_last_quote, 'USD')

last_date2, last_close2 = datetime.now(), -200
equity_last_quote2 = Quote(last_date2, last_close2)
equity.update_last_quote(equity_last_quote2)

#TODO: Create a custom exception after the PriorDateForUpdatingQuoteException that raised an error when the date
# of a quote used to update last quote for asset is before the current stored quote. Then modify the update last quote
# to store the quote in the quote history without updating the last quote attribute


"""
## Utility classes
    ** Definition/Concept**
        
    ** Why to use Utility it**
        
    ** When to use Utility Classes **
        
"""

import math
import statistics
import numpy as np

class FinancialAssetUtil:
    def calculate_one_period_return(self, initial_value: float, final_value: float, method= "simple"):
        """
        Calculates financial returns based on the one initial price and one final price.
        Parameters:
        - If two numerical arguments are provided:
        - Calculates simple or logarithmic return between two values.
        - Use method='simple' (default) for simple return.
        - Use method='log' for logarithmic return.
        Returns:
        - One return, type float.
        """
        if method == 'simple':
            return self.__calculate_simple_return(initial_value, final_value)
        elif method == 'log':
            return self.__calculate_log_return(initial_value, final_value)
        else:
            raise ValueError("Invalid method. Use 'simple' or 'log'.")

    def __calculate_simple_return(self, initial_value, final_value):
        return (final_value - initial_value) / initial_value

    def __calculate_log_return(self, initial_value, final_value):
        return math.log(final_value / initial_value)

    def calculate_volatility(self, returns):
        """
        Calculates the volatility (standard deviation) of a series of returns.

        Parameters:
        - returns: List or array of returns.

        Returns:
        - Volatility (standard deviation) of the returns.
        """
        if not isinstance(returns, (list, tuple)):
            raise ValueError("Returns must be a list or tuple.")
        if len(returns) < 2:
            raise ValueError("Returns list must contain at least two returns.")
        return statistics.stdev(returns)


    def calculate_drawdown(self, prices):
        """
        Calculates the drawdowns for a series of prices.

        Parameters:
        - prices: List of prices.

        Returns:
        - List of drawdown values.
        """
        if not isinstance(prices, list):
            raise ValueError("Prices must be a list.")
        peak = prices[0]
        drawdowns = []
        for price in prices:
            if price > peak:
                peak = price
            drawdown = (peak - price) / peak
            drawdowns.append(drawdown)
        return drawdowns

    def calculate_max_drawdown(self, prices):
        """
        Calculates the max drawdowns for a series of prices.

        Parameters:
        - prices: List of prices.

        Returns:
        - max drawdown value.
        """
        return np.max(self.calculate_drawdown(prices))


    def calculate_cumulative_return(self, returns):
        """
        Calculates the cumulative return from a series of returns.

        Parameters:
        - returns: List of returns.

        Returns:
        - Cumulative return value.
        """
        cumulative = 1.0
        for r in returns:
            cumulative *= (1 + r)
        return cumulative - 1



"""
## Static Methods: @staticmethod
    ** Definition/Concept** 

    ** Why to use it** 
       
    **   When to use it   ** 
"""


#TODO: modify the FinancialAssetUtil with static method


""" 
## Data class

    **Definition/Concept:**
       
    **Why to use it:**
   
    **When to use it:**
    
"""


"""
Example of a dataclass: Quote
To define a dataclass we use the decorator @dataclass. By doing so we no longer need to implement the init method or
other dunder method that are frequently implemented. Moreover if we perform an equality test for a dataclass, it will
check if all the attribute are the same and not if the instance of the two object are the same. 
"""

from dataclasses import dataclass


@dataclass
class Quote:
    date: datetime
    price: float


equity_last_quote = Quote(datetime(2023, 9, 29), 150)
print("str representation of dataclass")
print(str(equity_last_quote))
print("repr representation of dataclass")
print(repr(equity_last_quote))

equity_last_quote1 = Quote(datetime(2023, 9, 29), 150)
print("equal condition of dataclass")
print(equity_last_quote == equity_last_quote1)



"""
## Decorators
    ** Definition/Concept
        In Python, a decorator is a tagged that we put where a method is implemented that allows us to modify the 
        behavior of a function or class method without permanently modifying it. Decorators wrap a function, 
        augmenting or changing its behavior.
        In a nutshell, a decorator allow us to perform operation before or after the execution of a function.
        To applied a decorator to a function you will need to put an @ with the name of the decorator before the 
        implementation of the desired function (see example below)
    
    ### Why
        Decorators provide a way to extend a function's behavior without changing its source code. 
        This means you can reuse the same function in different contexts with different behaviors.
        
    ### When to use it
        Decorators are used when you want to wrap a function with additional functionality. 
        For example, you can use decorators to track execution time or check if a user is logged in before running 
        the function.
"""

"""
Example: how to implement and use a decorator
to implement a function based operator, you need to create a function which take a function as input and implement a
wrapper function in it. 
"""

def simple_decorator(func):  # here we defined a decorator
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


@simple_decorator  # here we applied the decorator to the function say_hello()
def say_hello():
    print("Hello, OOP course")

say_hello()

"""
** Decorators
Python provides several built-in decorators and others in its standard library. 
The most common are @staticmethod, @dataclass, @property, @classmethod
We already saw the first two one. Let's take a look at the other ones.

    @staticmethod
    The @staticmethod decorator is used for methods that don’t need access to the class or instance.
    
    @dataclass
    The @dataclass decorator, introduced in Python 3.7, automatically generates special methods like init(), repr(), 
    and eq() for a class

    @property
    The @property decorator is used to define methods in a class that act like attributes.
    
    @classmethod
    The @classmethod decorator is used to define methods that operate on the class rather than instances.
"""

"""
** @property Decorator

    ### Definition/Concept
       
    ### Why to use it
        
    ### When to use it
        

"""

class Position:
    def __init__(self, asset: FinancialAsset, initial_investment: float, current_value: float):
        self.asset = asset
        self.average_entry_price = initial_investment
        self.market_value = current_value

    @property
    def pnl(self):
        return self.market_value - self.average_entry_price


last_date, last_close = datetime.now(), 175.0
equity_last_quote = Quote(last_date, last_close)
equity = FinancialAsset('AAPL', equity_last_quote, 'USD')

position = Position(equity, 1000, 1250)
print(position.pnl)

#TODO: implement a new property which compute the total return of the position


"""
** @classmethod decorator
    ** Definition/Concept
       
    ** Why to use it
        
    ** When to use it
        
"""

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

date = Date.from_string("2024-07-29")
print(date.year)  # Output: 2024


"""
## Class-based Decorator
    ** Definition/Concept** 
    Class-based decorators use the functionality of objects to hold state or utilize inheritance for related decorator 
    logic. Essentially, a class-based decorator is a class that implements the __call__ method and the wrapper function. 
    When the instance of the class is called, the __call__ method is executed. The instance of the class is called
    before the method or function annotated by the decorator. 

    ** Why to use it** 
     - State Management: One of the biggest advantages of class-based decorators over function-based ones is the ability
                        to retain state. Since classes can have instance variables, it's easy to store and manage state
                        between calls.
                        
    - Reusability and Composition: Class-based decorators can utilize inheritance to create a family of related 
                                   decorators, or even compose multiple decorators together.
                                   
    - Enhanced Control: By defining other methods apart from __call__, you can provide more controlled or varied 
                        behavior, enhancing flexibility.

    ** When to use it  ** 
    - Stateful Decorations: When the decorator needs to remember something between calls, such as counting the number of 
                            times a function has been called or caching its results.
                            
    - Configurable Decorations: If you need to pass arguments to your decorator to configure its behavior. 
                                Though function-based decorators can also achieve this, class-based decorators can 
                                sometimes make this more intuitive, especially when there are many parameters or complex 
                                configurations.
                                
    - Multiple Related Decorators: If you are designing a suite of related decorators, it might be beneficial to 
                                encapsulate their shared logic within a base class and derive from it.
"""


class TradeLogger:
    def __init__(self, log_file='trade_log.txt'):
        self.log_file = log_file

    def __call__(self, execute_trade_func):
        def wrapper(*args, **kwargs):
            trade_result = execute_trade_func(*args, **kwargs)
            with open(self.log_file, 'a') as file:
                date = datetime.now()
                file.write(f"{date} - Trade Executed - Details: {trade_result}\n")
            return trade_result

        return wrapper


class Order:
    def __init__(self, ticker, quantity, order_type, order_status="CREATED", price_limit=None):
        self.ticker = ticker,
        self.qty = quantity,
        self.order_status = order_status,
        self.order_type = order_type
        self.price_limit = price_limit


class TradeExecutionService:
    @staticmethod
    @TradeLogger(log_file='../my_trades.txt')
    def execute_trade(order: Order):
        # For simplicity, we'll just return a dict of trade details.
        # In reality, the function might communicate with a brokerage API, handle order placement, etc.
        trade_details = {
            'ticker': order.ticker,
            'price': 100,
            'qty': order.qty,
            'order_type': order.order_type,
            'trade_status': "DONE"
        }
        return trade_details


# Executing a trade
order_0 = Order('FP FP Equity', -1000, "limit", price_limit=99.95)
trade_details = TradeExecutionService.execute_trade(order_0)



