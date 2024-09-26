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


