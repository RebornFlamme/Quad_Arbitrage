import ccxt

def get_pairs(exchange_name):

    exchange = getattr(ccxt, exchange_name)()

    exchange_tickers = exchange.fetch_tickers()
    if len(exchange_tickers) > 0:
        tickers_list = []
        for ticker in exchange_tickers.keys():
            tickers_list.append(ticker)

        filtered_tickers = [ticker for ticker in tickers_list if not ticker.endswith(('USD', 'EUR', 'GBP'))]
    else:
        print("Error retrieving tickers")

    return filtered_tickers




