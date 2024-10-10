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


class MomentumStrategy(Strategy):
    def __init__(self, lookback_period: int):
        self.lookback_period = lookback_period  # Number of periods to look back for momentum calculation

    def generate_signals(self, position_for_signal_generation: dict):
        signals = {}

        for ticker, position in position_for_signal_generation.items():
            instrument = position.instrument
            df_prices = instrument.quotes_to_dataframe()

            df_prices.sort_index(inplace=True)
            df_prices['AvgPrice'] = df_prices['Price'].rolling(window=self.lookback_period).mean()
            df_prices['Momentum'] = df_prices['Price'] - df_prices['AvgPrice']

            df_prices['Signal'] = 0
            df_prices.loc[df_prices['Momentum'] > 0, 'Signal'] = 1
            df_prices.loc[df_prices['Momentum'] < 0, 'Signal'] = -1

            latest_date = df_prices.index[-1]
            latest_signal = df_prices.at[latest_date, 'Signal']
            signals[ticker] = latest_signal

        return signals