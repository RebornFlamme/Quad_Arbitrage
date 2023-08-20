import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def generate_adjacency_matrix(input_data, coin_dict):
    symbols = []
    adjacency_map = {}

    for line in input_data:
        try:
            s1, s2 = line.split("/")
        except:
            continue
        
        if s1 not in symbols:
            symbols.append(s1)
        if s2 not in symbols:
            symbols.append(s2)

        if s1 not in adjacency_map:
            adjacency_map[s1] = []
        if s2 not in adjacency_map:
            adjacency_map[s2] = []

        if s2 not in adjacency_map[s1]:
            adjacency_map[s1].append(s2)

        if s1 not in adjacency_map[s2]:
            adjacency_map[s2].append(s1)

    num_symbols = len(symbols)
    
    adjacency_matrix = np.zeros((num_symbols, num_symbols), dtype=float) 

    for source_symbol, connected_symbols in adjacency_map.items():
        source_index = symbols.index(source_symbol)
        for connected_symbol in connected_symbols:
            connected_index = symbols.index(connected_symbol)

            for ticker in coin_dict.keys():
                ticker_split = ticker.split("/")
                if source_symbol in ticker_split and connected_symbol in ticker_split:
                    if source_symbol == ticker_split[0] and connected_symbol == ticker_split[1]:
                        adjacency_matrix[source_index, connected_index] = float(coin_dict[ticker]['Ask'])
                    if source_symbol == ticker_split[0] and connected_symbol == ticker_split[1]:
                         adjacency_matrix[source_index, connected_index] = 1.0 / float(coin_dict[ticker]['Bid'])
                    

            #adjacency_matrix[source_index, connected_index] = 1
    
    return symbols, adjacency_matrix


def plot_graph(symbols, adjacency_matrix):
    print(adjacency_matrix)
    # Create a graph from the adjacency matrix
    G = nx.Graph()
    for i, coin in enumerate(symbols):
        G.add_node(coin)
        for j in range(i + 1, len(symbols)):
            if adjacency_matrix[i, j] < 1000000000000.0:
                
                G.add_edge(symbols[i], symbols[j])

    # Draw the graph
    pos = nx.spring_layout(G, seed=42)  # You can choose other layout algorithms
    nx.draw(G, pos, with_labels=True, node_size=100, font_size=6, font_color='black')
    plt.title("Crypto Coin Pairs Graph")
    plt.show()


def find_paths(adjacency_matrix, symbols, start_symbol, end_symbol):
    start_index = symbols.index(start_symbol)
    end_index = symbols.index(end_symbol)
    
    stack = [(start_index, [start_index])]

    paths = []

    while stack:
        current_index, current_path = stack.pop()

        if current_index == end_index and len(current_path) == 5:
            paths.append(current_path)
            continue

        if len(current_path) >= 5:
            continue

        connected_indices = np.nonzero(adjacency_matrix[current_index])[0]

        for connected_index in connected_indices:
            if connected_index not in current_path:
                stack.append((connected_index, current_path + [connected_index]))

    return paths


#show_graph_with_labels(adjacency, make_label_dict(get_labels(symbols)))

# paths = find_paths(adjacency_matrix, symbols, start_symbol, end_symbol)

# formatted_paths = []

# for path in paths:
#   formatted_path = []
  
#   for i in range(len(path)):
#     if i >= len(path) - 1:
#       break
#     formatted_path.append("/".join([symbols[path[i]], symbols[path[i + 1]]]))

#   formatted_paths.append(formatted_path)


# print(formatted_paths)
