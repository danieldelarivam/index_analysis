from index_analysis.data.market import Market
from index_analysis.data.yahoo_market import YahooMarket
from index_analysis.data.yahoo_market import TWSMarket

def get_market(config: dict) -> Market:
    if config["impl_type"] == "yahoo":
        return YahooMarket(config)
    elif config["impl_type"] == "tws":
        return TWSMarket(config)

