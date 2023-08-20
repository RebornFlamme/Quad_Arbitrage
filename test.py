import ccxt
import json

exchange = ccxt.kucoin()
print(exchange.fetch_ticker('BTC/USDT'))


script_directory = os.path.dirname(os.path.abspath(__file__))

    # Specify the file name for storing the data
json_file_name = "stored_data.json"

    # Combine the directory and file name to create the full file path
json_file_path = os.path.join(script_directory, json_file_name)

    # Write the data to the JSON file
with open(json_file_path, "w") as json_file:
    json.dump(data_to_store, json_file)




with open(json_file_path, "r") as json_file:
    stored_data = json.load(json_file)