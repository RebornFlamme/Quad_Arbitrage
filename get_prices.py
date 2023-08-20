import ccxt
import os
import json

def get_prices(exchange_name, coin_list):

    exchange = getattr(ccxt, exchange_name)()
    coin_dict = {}
    
    i = 1

    for ticker in coin_list:

        try : 
            coin = exchange.fetch_ticker(ticker)
            bid_price = coin['bid']
            ask_price = coin['ask']

            coin_dict[f'{ticker}'] = {}
            coin_dict[f'{ticker}']['Bid'] = bid_price
            coin_dict[f'{ticker}']['Ask'] = ask_price

            print(f'{ticker} OK {i}/{len(coin_list)} processed')
        except:
            print(f"Error while retrieving the price of {ticker}")

        i += 1


    script_directory = os.path.dirname(os.path.abspath(__file__))

    json_file_name = "coin_dict.json"

    json_file_path = os.path.join(script_directory, json_file_name)

    # Write the data to the JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(coin_dict, json_file)
        
    print(coin_dict)
    return coin_dict