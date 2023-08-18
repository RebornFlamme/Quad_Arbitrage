import pandas as pd
import numpy as np 
import ccxt as ccxt
import time

kraken = ccxt.kraken()
kucoin = ccxt.kucoin()
binance = ccxt.binance()

from get_pairs import get_pairs
from structure_pairs import structure_quad_pairs
from pairs_map import generate_adjacency_matrix
from pairs_map import plot_graph


coin_list = get_pairs(kucoin)
print(coin_list)


symbols, adjacency_matrix = generate_adjacency_matrix(coin_list)

plot_graph(symbols, adjacency_matrix)

