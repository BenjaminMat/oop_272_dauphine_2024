from dataclasses import dataclass

from datetime import datetime
import pandas as pd
import yfinance as yf

"""
**Exercise 4: Constructing a DataClass for Yahoo Finance**

**Objective**: Design a DataClass to encapsulate data related to Yahoo Finance and implement a method in the 
YahooFinanceDataLoader to fetch and populate this data.

**Steps**:

1. **Define the DataClass**:   
   Construct a DataClass named YahooFinanceData. This class should encapsulate the following attributes:
   - ticker: Represents the stock ticker.
   - short_name: Provides a short name for the stock.
   - sector: Designates which sector the stock belongs to.
   - market_cap: Specifies the market capitalization of the stock.
   - currency: Notes the currency used.
   - dividend_yield: Indicates the dividend yield of the stock.
   - short_ratio: Denotes the short ratio.
   - price_history: Contains the historical price data of the stock.
   
   After creating the dataclass, create a classmethod method which takes the following argument and build the object 
   data: dict, ticker: str, history: pd.DataFrame. data will contain short_name, sector, ...

2. **Enhance the YahooFinanceDataLoader**:
   Extend the YahooFinanceDataLoader class to integrate a new method named populate_dataclass. This method should:
   - Fetch all the necessary data points required to populate the YahooFinanceData dataclass.
   - Use the yFinance.info object to retrieve all the information. Except for the price_history, all the information 
   could be retrieve from the yFinance.info object (example : for short_name it will be ticker.info.shortName. transform
   the snake_case notation to a camelCase notation)
   - For the price history, you can use the method already defined in the data loader

3. **Instance Creation and Population**:
   - Instantiate an object YahooFinanceDataLoader.
   - Use the populate_dataclass method of the YahooFinanceDataLoader to create a YahooFinanceData object.
   
Hint: 
    Start by trying all the method of the data loader. You could also use it on debug to see the attribute of the
    object you retrieve from yahoo finance.
    If you have difficulties when you try to import yfinance package, go to the other/yfinance_installation.txt file.
"""


class MarketDataDownloadError(Exception):
    """An error raised when there's a problem downloading market data."""

    def __init__(self, cls, method, *args):
        self.cls = cls
        self.method = method
        self.args = args

    def __str__(self):
        return f"Error in class '{self.cls.__name__}', method '{self.method}' with arguments {self.args}"


class YahooFinanceDataLoader:
    @staticmethod
    def get_information_for_ticker(yahoo_ticker) -> yf.Ticker:
        """method to get the information relative to a Yahoo ticker. Raises an exception if ticker doesn't exist."""
        try:
            ticker = yf.Ticker(yahoo_ticker)
            ticker.info
            return ticker
        except Exception:  # This is a general catch-all for exceptions not specified above
            raise MarketDataDownloadError(YahooFinanceDataLoader, 'get_information_for_ticker', yahoo_ticker)

    @staticmethod
    def get_last_close_and_date(ticker_symbol) -> (datetime, float):
        ticker = YahooFinanceDataLoader.get_information_for_ticker(ticker_symbol)
        try:
            hist = ticker.historys(period="1d")  # correct implementation : hist = ticker.history(period="1d")

            last_date_for_symbol = hist.index[0]
            last_close_for_symbol = hist['Close'][0]

            return last_date_for_symbol, last_close_for_symbol

        except Exception:  # This is a general catch-all for exceptions not specified above
            raise MarketDataDownloadError(YahooFinanceDataLoader, 'get_last_close_and_date', ticker_symbol)

    @staticmethod
    def historical_price(ticker_symbol, start_date=None, end_date=None) -> pd.DataFrame:
        try:
            ticker = YahooFinanceDataLoader.get_information_for_ticker(ticker_symbol)
            return ticker.history(period="1d", start=start_date, end=end_date)
        except Exception:  # This is a general catch-all for exceptions not specified above
            raise MarketDataDownloadError(YahooFinanceDataLoader, 'historical_price', ticker_symbol)


if __name__ == '__main__':
    loader = YahooFinanceDataLoader()
    data = loader.populate_dataclass('MMM')