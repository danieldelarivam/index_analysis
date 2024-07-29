from index_analysis.data.market import Market
import yfinance as yf

class YahooMarket(Market):

    def __init__(self, config: dict):
        """
        Constructor that initializes the market data.

        :param config: configuration dictionary.
        """
        self._config = config

    def get_data(self, stock_name: str, start: str, end: str):
        return yf.download(stock_name, start=start, end=end).head()
