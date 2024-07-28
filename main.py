import yaml
from index_analysis.data.market import Market
from index_analysis.data import get_market

def read_config(config_file: str) -> dict:
    """
    Function that reads the configuration file.

    :param config_file: configuration file.
    :return: configuration dictionary.
    """
    with open(config_file, "r") as file:
        return yaml.safe_load(file)

def main():
    # create a market object
    market: Market = get_market(read_config("config.yml"))
    a: int = 1

    # get the historical data
    data = market.get_data(stock_name="AAPL", start="2024-03-01", end="2024-07-03")

    # print the data
    print("Historical data about the market, for stock name AAPL:")
    print(data)


if __name__ == "__main__":
    main()
