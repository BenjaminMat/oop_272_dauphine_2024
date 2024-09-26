import math
from datetime import datetime
import pandas as pd

from exercise.s4.s4_resources.instrument import Instrument
from exercise.s4.s4_resources.strategy import Strategy


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

