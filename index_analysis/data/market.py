"""
Module that provides historical data about the market.
"""

import pandas as pd
import datetime as dt
from abc import ABC, abstractmethod

# class MarketResult:
#     Open        High         Low       Close   Adj Close    Volume

class Market(ABC):
    """
    Market class that provides historical data about the market.
    """
    @abstractmethod
    def get_data(self, stock_name: str, start: str, end: str) -> pd.DataFrame:
        """
        Method that returns the historical data about the market.

        :param stock_name: name of the stock.
        :param start: start date of the data, in the format 'YYYY-MM-DD'.
        :param end: end date of the data, in the format 'YYYY-MM-DD'.
        :return: historical data about the market.

        The return type is a Pandas DataFrame with four columns:
        Open        High         Low       Close   Adj Close    Volume
        """

