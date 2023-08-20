from typing import List, Tuple
from math import log

def negate_logarithm_convertor(graph: List[List[float]]) -> List[List[float]]:
    ''' log of each rate in graph and negate it'''
    #result = [[-log(edge) for edge in row] for row in graph]
    result = [[-log(edge) if edge > 0 else float('inf') for edge in row] for row in graph]

    return result

def arbitrage(symbol_list: List[str], adjacency_matrix: List[List[float]]):
    ''' Calculates arbitrage situations and prints out the details of this calculation'''

    trans_graph = negate_logarithm_convertor(adjacency_matrix)

    source = 0
    n = len(trans_graph)
    min_dist = [float('inf')] * n
    pre = [-1] * n
    min_dist[source] = source

    for _ in range(n - 1):
        for source_curr in range(n):
            for dest_curr in range(n):
                if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                    min_dist[dest_curr] = min_dist[source_curr] + trans_graph[source_curr][dest_curr]
                    pre[dest_curr] = source_curr

    for source_curr in range(n):
        for dest_curr in range(n):
            if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                print_cycle = [dest_curr, source_curr]
                while pre[source_curr] not in print_cycle:
                    print_cycle.append(pre[source_curr])
                    source_curr = pre[source_curr]
                print_cycle.append(pre[source_curr])
                print("Arbitrage Opportunity:")
                print(" --> ".join([symbol_list[p] for p in print_cycle[::-1]]))

