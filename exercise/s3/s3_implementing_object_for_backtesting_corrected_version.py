"""
TP Instructions: Implementing a Strategy and a Portfolio for a backtesting task

Objective:
You need to implement methods and functionalities for a Portfolio class. The class should handle the operations
of initializing the portfolio with financial instrument, rebalancing its positions based on a given strategy,
and providing a summary of the portfolio positions.

Tips:
    - Use the methods and attributes of other provided classes like Instrument, Quote, and Position.
    - Before starting the exercise be sure to fully understand how the object provided for it worked.
    - Remember to handle cases where certain attributes might be None or missing.
    - If you finish the exercise early, you can implement method to populate the attribute of the Portfolio class
    that are not handle yet.
"""

from datetime import datetime
import pandas as pd


class Quote:
    def __init__(self, date: datetime, price: float):
        self.date = date
        self.price = price

    def __str__(self):
        return f'(date: {self.date}, price: {self.price})'


class Instrument:
    def __init__(self, ticker: str, exchange: str, quote: Quote, currency: str):
        self.ticker: str = ticker
        self.exchange: str = exchange
        self.last_quote: Quote = quote
        self.currency: str = currency
        self.quote_history: [Quote] = []

    def __str__(self):
        print(f'Instrument with ticker {self.ticker}, currency {self.currency} and last quote {self.last_quote}')

    def update_price(self, new_quote: Quote):
        self.quote_history.append(self.last_quote)
        self.last_quote = new_quote

    def populate_quote_history_from_df(self, df_data: pd.DataFrame):
        dates = df_data.index.to_pydatetime().tolist()
        prices = df_data['Close'].tolist()
        self.quote_history = [Quote(date, price) for date, price in zip(dates, prices)]

    def quotes_to_dataframe(self) -> pd.DataFrame:
        data = {
            "Date": [quote.date for quote in self.quote_history],
            "Price": [quote.price for quote in self.quote_history]
        }
        df = pd.DataFrame(data)
        df.set_index('Date', inplace=True)
        return df


class Position:
    def __init__(self, instrument: Instrument, date: datetime = datetime.now(), weight: float = 0, quantity: float = 0):
        self.instrument = instrument
        self.date = date
        self.weight = weight
        self.quantity = quantity

    def update(self, date: datetime, weight: float, quantity: float):
        if date is not None:
            self.date = date
        if weight is not None:
            self.weight = weight
        if quantity is not None:
            self.quantity = quantity


"""
PART I: Creating the meta class strategy and one specific strategy:
Create an abstract class Strategy that will serve as the base for all strategies. 

This class should:
    Include an abstract method generate_signals that will generate trading signals based on input data.
    Document the method generate_signals with a docstring explaining the parameters and return value (see below):
        Parameters for the class : A dictionary with tickers as keys and positions as values. The dict should be named 
                                   data_for_signal_generation
        Return: A dictionary with tickers as keys and signals as values.

Create a derived class EqualWeightStrategy from Strategy:
    This class should inherit from Strategy and implement the generate_signals method.
    It should calculate and return a dictionary with equal-weight signals for each ticker.

To Implement the generate_signals method:
    The method should calculate equal-weight signals for each ticker by dividing 1 by the total number of tickers.
    It should return a dictionary where each ticker has an equal weight as its signal.
"""

from datetime import datetime
import math
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def generate_signals(self, data_for_signal_generation: dict):
        """
        Method aims to generate signals for backtesting strategy.

        Parameters for the class : A dictionary with tickers as keys and positions as values. The dict should be named
                                   data_for_signal_generation
        Return: A dictionary with tickers as keys and signals as values.
        """
        pass

class EqualWeightStrategy(Strategy):

    def generate_signals(self, data_for_signal_generation: dict):
        #{expression which generate a dict for item in iterable if condition} for creating a dict
        tickers = data_for_signal_generation.keys()
        equal_wgt = 1 / len(tickers)
        return {ticker: equal_wgt for ticker in tickers}



"""
Part II : Creating the Portfolio class:

Class Attributes: Based on the provided code framework, create a Portfolio class which should have the following attributes:
                name: Name of the portfolio.
                currency: The currency in which the portfolio is denominated.
                aum: Assets Under Management.
                nav : The last net asset value computed for the portfolio
                historical_nav: A list that keeps track of the historical Net Asset Values.
                positions: A list of Position objects representing the portfolio’s assets.
                strategy: A strategy object, an instance of a class derived from the Strategy class.
                Initialization: Implement the __init__ method to initialize the portfolio attributes.

Initialize Portfolio Positions: 
Implement a initialize_position_from_instrument_list method to initialize the portfolio’s positions with a given 
list of Instrument objects. Each Instrument should be wrapped in a Position object.

Positions to Dictionary: Implement the _positions_to_dict method which returns a dictionary of positions with 
ticker symbols as keys and Position objects as values. This will help in rebalancing operations.

Rebalancing: Implement the rebalance_portfolio method which performs the following tasks:
    Convert the positions list into a dictionary.
    Generate trading signals using the provided strategy.
    Update the weight and quantity of each position in the portfolio based on the generated signals.

Portfolio Summary: Implement the portfolio_position_summary method. This method should return a dataframe 
    summarizing the portfolio’s current positions, including the ticker symbols, weights, quantities, 
    and last close for the assets
"""



class Portfolio:
    def __init__(self, name: str, currency: str, aum: float, nav: float, portfolio_strategy: Strategy):
        self.name: str = name
        self.currency: str = currency
        self.aum: float = aum
        self.nav: float = nav
        self.historical_nav = []
        self.positions: [Position] = []
        self.strategy = portfolio_strategy

    def _positions_to_dict(self) -> dict:
        return {position.instrument.ticker: position for position in self.positions if position.weight is not None}

    def initialize_position_from_instrument_list(self, instrument_list: list[Instrument]):
        self.positions = [Position(instrument) for instrument in instrument_list]

    def rebalance_portfolio(self, rebalancing_date: datetime = None):
        if rebalancing_date is None:
            rebalancing_date = datetime.now()

        positions_dict = self._positions_to_dict()
        signals = self.strategy.generate_signals(positions_dict)

        for position in self.positions:
            ticker = position.instrument.ticker
            weight = signals.get(ticker, 0)
            new_quantity = math.floor((self.aum * weight) / position.instrument.last_quote.price)
            position.update(quantity=new_quantity, weight=weight, date=rebalancing_date)

    def portfolio_position_summary(self) -> pd.DataFrame:
        tickers = [position.instrument.ticker for position in self.positions]
        weights = [position.weight for position in self.positions]
        quantities = [position.quantity for position in self.positions]
        last_prices = [position.instrument.last_quote.price for position in self.positions]

        data = {
            "Ticker": tickers,
            "Weight": weights,
            "Quantity": quantities,
            "Last close": last_prices
        }
        return pd.DataFrame(data)




import unittest

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        # Setup the instruments and quotes
        self.last_date_asset_1 = datetime(2024, 8, 29)
        self.last_close_asset_1 = 230.02
        self.equity_last_quote_asset_1 = Quote(self.last_date_asset_1, self.last_close_asset_1)
        self.equity_1 = Instrument('AAPL', 'NASDAQ', self.equity_last_quote_asset_1, 'USD')

        self.last_date_asset_2 = datetime(2024, 8, 29)
        self.last_close_asset_2 = 414.75
        self.equity_last_quote_asset_2 = Quote(self.last_date_asset_2, self.last_close_asset_2)
        self.equity_2 = Instrument('MSFT', 'NASDAQ', self.equity_last_quote_asset_2, 'USD')

        # Update prices
        self.last_date_asset_1 = datetime(2024, 8, 30)
        self.last_close_asset_1 = 229.0
        self.equity_1.update_price(Quote(self.last_date_asset_1, self.last_close_asset_1))

        self.last_date_asset_2 = datetime(2024, 8, 30)
        self.last_close_asset_2 = 417.14
        self.equity_2.update_price(Quote(self.last_date_asset_2, self.last_close_asset_2))

        # Setup the portfolio strategy and portfolio
        self.pft_strategy = EqualWeightStrategy()
        self.portfolio = Portfolio("Tech Portfolio", "USD", 1000000, 10000, self.pft_strategy)
        self.portfolio.initialize_position_from_instrument_list([self.equity_1, self.equity_2])

    def test_initial_portfolio_summary(self):
        # Test the initial summary of the portfolio
        summary = self.portfolio.portfolio_position_summary()
        expected_data = {
            "Ticker": ['AAPL', 'MSFT'],
            "Weight": [0, 0],
            "Quantity": [0, 0],
            "Last close": [229.0, 417.14]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(summary, expected_df)

    def test_rebalance_portfolio(self):
        # Rebalance the portfolio and check the summary
        self.portfolio.rebalance_portfolio()
        summary = self.portfolio.portfolio_position_summary()

        # Calculate expected values
        total_aum = self.portfolio.aum
        expected_weight = 0.5
        expected_quantity_1 = math.floor((total_aum * expected_weight) / self.equity_1.last_quote.price)
        expected_quantity_2 = math.floor((total_aum * expected_weight) / self.equity_2.last_quote.price)

        expected_data = {
            "Ticker": ['AAPL', 'MSFT'],
            "Weight": [expected_weight, expected_weight],
            "Quantity": [expected_quantity_1, expected_quantity_2],
            "Last close": [229.0, 417.14]
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(summary, expected_df)



def run_tests():
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    run_tests()
