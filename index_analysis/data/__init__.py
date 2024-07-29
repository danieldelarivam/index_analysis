from index_analysis.data.market import Market
from index_analysis.data.yahoo_market import YahooMarket

def get_market(config: dict) -> Market:
    if config["options"]["market_implementation"] == "yahoo":
        return YahooMarket(config)
    elif config["market_implementation"] == "tws":
        return TWSMarket(config)

