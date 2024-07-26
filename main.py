from index_analysis.data.market import Market


def main():
    # create a market object
    market = Market(config={})

    # get the historical data
    data = market.get_data(stock_name="AAPL", start="2021-01-01", end="2021-01-03")

    # print the data
    print("Historical data about the market, for stock name AAPL:")
    print(data)


if __name__ == "__main__":
    main()
