"""
Module that provides historical data about the market.
"""

import pandas as pd
import datetime as dt


class Market:
    """
    Market class that provides historical data about the market.
    """

    def __init__(self, config: dict):
        """
        Constructor that initializes the market data.

        :param config: configuration dictionary.
        """
        self._config = config

    def get_data(self, stock_name: str, start: str, end: str):
        """
        Method that returns the historical data about the market.

        :param stock_name: name of the stock.
        :param start: start date of the data, in the format 'YYYY-MM-DD'.
        :param end: end date of the data, in the format 'YYYY-MM-DD'.
        :return: historical data about the market.
        """

        # return a mock data frame for now
        return pd.DataFrame(
            {
                "Date": [
                    dt.datetime.now() - dt.timedelta(days=3),
                    dt.datetime.now() - dt.timedelta(days=2),
                    dt.datetime.now() - dt.timedelta(days=1),
                ],
                "Open": [100, 101, 102],
                "High": [105, 106, 107],
                "Low": [95, 96, 97],
                "Close": [102, 103, 104],
                "Volume": [100000, 200000, 300000],
            }
        )
