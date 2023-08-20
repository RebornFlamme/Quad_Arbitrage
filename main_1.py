import pandas as pd
import numpy as np 
import ccxt as ccxt
import time
import json
import os
from typing import Tuple, List
from math import log


kraken = ccxt.kraken()
kucoin = ccxt.kucoin()
binance = ccxt.binance()

from get_pairs import get_pairs
from structure_pairs import structure_quad_pairs
from pairs_map import generate_adjacency_matrix
from pairs_map import plot_graph
from get_prices import get_prices
from bellman_ford import arbitrage

import numpy as np

coin_list = get_pairs('kucoin')
# coin_dict = get_prices('kucoin', coin_list)

script_directory = os.path.dirname(os.path.abspath(__file__))
json_file_name = "coin_dict.json"
json_file_path = os.path.join(script_directory, json_file_name)

with open(json_file_path, "r") as json_file:
    coin_dict = json.load(json_file)


symbols, adjacency_matrix = generate_adjacency_matrix(coin_list, coin_dict)

print(adjacency_matrix)

# Call the function with the modified names
#arbitrage(symbols, adjacency_matrix)

plot_graph(symbols, adjacency_matrix)