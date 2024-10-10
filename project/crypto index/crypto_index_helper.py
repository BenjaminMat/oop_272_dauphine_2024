from datetime import datetime

import pandas as pd
import pycoingecko
from binance import Client

"""
pip install pytest responses
pip install -U pycoingecko
pip install python-binance


package documentation: https://pypi.org/project/pycoingecko/
https://python-binance.readthedocs.io/en/latest/overview.html

"""


if __name__ == "__main__":
    from pycoingecko import CoinGeckoAPI
    import time

    # Example of CoinGecko
    coin_gecko_api = CoinGeckoAPI()

    id_coin = 'bitcoin'
    reference_fiat_currency = "usd"

    data_coin = coin_gecko_api.get_coin_by_id(id_coin)
    tag_for_coin = data_coin['categories']

    # Example of Binance
    binance_client = Client()
    dataset = pd.read_csv("/project/crypto index/coin_data_from_CoinGecko.csv") # put the path of the csv file instead of "/project/crypto index/coin_data_from_CoinGecko.csv"
    ticker_list = (dataset['base']+dataset['target']).tolist()  # getting available coin tickers from CoinGecko stored data

    # Tickers are built to retrieve the price of a cryptocurrency pair. For example, BTCUSDT retrieves the price of BTC
    # vs USDT and ETHEUR the price of ETH against EUR. Cryptocurrencies are always quoted in pairs.

    start_date_str = "1 Jan, 2019"
    end_date_str = "1 Jan, 2024"
    ticker = ticker_list[0]
    result_binance = []
    for k_line in binance_client.get_historical_klines_generator(symbol=ticker,
                                                                 interval=Client.KLINE_INTERVAL_1DAY,
                                                                 start_str=start_date_str, end_str=end_date_str):
        result_binance.append(k_line) #you can check the api documentation to see the data return by the klines

    columns = [
        'Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
        'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
        'Taker buy quote asset volume', 'Ignore'
    ]

    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote asset volume',
                       'Number of trades', 'Taker buy base asset volume',
                       'Taker buy quote asset volume']

    df = pd.DataFrame(result_binance, columns=columns)
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')
    df.drop(columns=['Ignore'], inplace=True)
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    end = True




