import sys

import networkx as nx
from graphs import GraphFord, GraphKhun, Edge
from bipartite import graph_to_bipartite


edges = [(4, 7), (3, 16), (4, 16), (8, 11), (12, 14), (7, 8), (7, 13),
         (6, 15), (11, 14), (7, 15), (9, 11), (5, 12), (8, 16),
         (4, 6), (6, 8), (4, 11), (6, 13), (2, 6), (4, 12), (7, 9),
        (8, 12), (10, 11), (12, 13), (5, 16), (15, 16), (2, 16),
        (7, 10), (5, 7), (9, 16), (11, 15), (3, 6), (7, 14),
        (10, 16), (2, 11), (3, 11)
    ]

gr = nx.Graph(edges)
if not nx.is_bipartite(gr):
    edges = graph_to_bipartite(edges)
    gr = nx.Graph(edges)
    if not nx.is_bipartite(gr):
        sys.exit("Graph is not bipartite")

x, y = nx.bipartite.sets(gr)
print(f'u={list(x)}, v={list(y)}')
graph_ford = GraphFord(len(x) + len(y) + 2)
for edge in edges:
    if edge[0] in x and edge[1] in y:
        graph_ford.add_edge(edge[0] - 1, edge[1] - 1)
    else:
        graph_ford.add_edge(edge[1] - 1, edge[0] - 1)

for node in x:
    graph_ford.add_edge(0, node - 1)

for node in y:
    graph_ford.add_edge(node - 1, max(list(x) + list(y)))

print("Ford_Fulkerson")
max_matching_ford, matching_edges = graph_ford.find_matching_ford()
print("max_matching: ", max_matching_ford)
print("matching_edges: ", end='')
for edge in matching_edges:
    if 0 not in edge and 16 not in edge:
        edge = (edge[0] + 1, edge[1] + 1)
        print(edge, end=' ')
print()

print("Khun")
graph_khun = GraphKhun(len(x) + len(y))
for edge in edges:
    if edge[0] in x and edge[1] in y:
        graph_khun.add_edge(edge[0] - 2, edge[1] - 2)
    else:
        graph_khun.add_edge(edge[1] - 2, edge[0] - 2)


max_matching_khun = graph_khun.find_matching_khun()
max_matching_set = []
for i in range(len(max_matching_khun)):
    edge = Edge(i, max_matching_khun[i]) if max_matching_khun[i] != -1 else None
    if not edge  is None:
        if len(max_matching_set) == 0:
            max_matching_set.append(edge)
            continue
        if edge not in max_matching_set:
            max_matching_set.append(edge)

for i in max_matching_set:
    print(f'({i.u + 2}, {i.v + 2}) ', end='')


if __name__ == '__main__':
    ...