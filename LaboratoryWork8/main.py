import networkx as nx
import random

import graph
import prepare_network



def new_network(original_adjacency_list: dict[str, list[tuple[str, int]]]) -> dict[str, list[tuple[str, int]]]:
    for node in original_adjacency_list.keys():
        for i in range(len(original_adjacency_list[node])):
            if original_adjacency_list[node][i][1] != 0:
                original_adjacency_list[node][i] = (original_adjacency_list[node][i][0], random.randint(100, 1000))

    return original_adjacency_list


original_network = {
    'A':  [('A', 0),   ('B', 5),   ('C', 9),   ('D', 0),   ('E', 0),   ('F', 0),   ('G', 0),   ('H', 0),   ('I', 4)],
    'B':  [('A', 0),   ('B', 0),   ('C', 2),   ('D', 0),   ('E', 0),   ('F', 0),   ('G', 2),   ('H', 0),   ('I', 2)],
    'C':  [('A', 0),   ('B', 0),   ('C', 0),   ('D', 0),   ('E', 0),   ('F', 0),   ('G', 0),   ('H', 0),   ('I', 0)],
    'D':  [('A', 0),   ('B', 0),   ('C', 2),   ('D', 0),   ('E', 0),   ('F', 0),   ('G', 0),   ('H', 0),   ('I', 0)],
    'E':  [('A', 0),   ('B', 0),   ('C', 0),   ('D', 7),   ('E', 0),   ('F', 0),   ('G', 0),   ('H', 0),   ('I', 0)],
    'F':  [('A', 0),   ('B', 0),   ('C', 2),   ('D', 7),   ('E', 7),   ('F', 0),   ('G', 0),   ('H', 0),   ('I', 0)],
    'G':  [('A', 0),   ('B', 0),   ('C', 7),   ('D', 3),   ('E', 3),   ('F', 3),   ('G', 0),   ('H', 0),   ('I', 0)],
    'H':  [('A', 0),   ('B', 0),   ('C', 7),   ('D', 0),   ('E', 0),   ('F', 7),   ('G', 7),   ('H', 0),   ('I', 0)],
    'I':  [('A', 0),   ('B', 0),   ('C', 4),   ('D', 0),   ('E', 0),   ('F', 0),   ('G', 2),   ('H', 7),   ('I', 0)]
}

letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}




print("networkx methods")

network2 = prepare_network.create_graph(original_network)
start2 = prepare_network.find_start(network2)
end2 = prepare_network.find_end(network2)

print(f"source: {start2}, sink: {end2}")
print("maximum_flow", nx.maximum_flow(network2, start2, end2)[0])
print("minimum_cut", nx.minimum_cut(network2, start2, end2))
print()

print("my realization")

network = graph.create_graph(original_network)
start = graph.find_start(network)
end = graph.find_end(network)
max_flow = network.ford_fulkerson(start, end)
min_cut = network.min_cut(start)
for i in range(len(min_cut[0])):
    min_cut[0][i] = (list(letters.keys())[min_cut[0][i][0]], list(letters.keys())[min_cut[0][i][1]])

print(f"source: {list(letters.keys())[start]}, sink: {list(letters.keys())[end]}")
print("maximum_flow", max_flow)
print("minimum_cut", min_cut)
print()

print("network with 100 - 1000 capacity")
big_network = new_network(original_network)

print("networkx methods")

big_networkx = prepare_network.create_graph(big_network)
start_big = prepare_network.find_start(big_networkx)
end_big = prepare_network.find_end(big_networkx)

print(f"source: {start_big}, sink: {end_big}")
print("maximum_flow", nx.maximum_flow(big_networkx, start_big, end_big)[0])
print("minimum_cut", nx.minimum_cut(big_networkx, start_big, end_big))

print()

my_big_network = graph.create_graph(big_network)
my_start_big = graph.find_start(my_big_network)
my_end_big = graph.find_end(my_big_network)
max_flow = my_big_network.ford_fulkerson(my_start_big, my_end_big)
min_cut = my_big_network.min_cut(my_start_big)
for i in range(len(min_cut[0])):
    min_cut[0][i] = (list(letters.keys())[min_cut[0][i][0]], list(letters.keys())[min_cut[0][i][1]])

print(f"source: {list(letters.keys())[start]}, sink: {list(letters.keys())[end]}")
print("maximum_flow", max_flow)
print("minimum_cut", min_cut)
print()

if __name__ == '__main__':
    ...


