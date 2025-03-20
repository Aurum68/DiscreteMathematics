import maxFullSubgraph, graphAdding


graph = [(0, 1), (0, 4), (0, 6), (1, 2), (1, 7), (5, 1), (2, 7),
 (2, 3), (5, 3), (3, 4), (4, 5), (5, 7), (5, 6), (6, 7)]

if __name__ == '__main__':
    print("Полные подграфы")
    maxFullSubgraph.max_full_subgraph(graph)
    print("Ребра дополнения")
    graphAdding.graph_adding(graph)