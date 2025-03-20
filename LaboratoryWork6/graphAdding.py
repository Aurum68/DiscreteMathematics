import itertools
from maxFullSubgraph import vertex_list

def create_adding_list(graph: list[tuple[int, int]], vertex: list[int]) -> dict[int, set[int]]:
    adding_list = {}
    pairs = list(itertools.combinations(vertex, 2))
    for pair in pairs:
        if pair[0] == pair[1]:
            continue
        if pair not in graph and (pair[1], pair[0]) not in graph:
            if pair[0] not in list(adding_list.keys()):
                adding_list[pair[0]] = set()
            adding_list[pair[0]].add(pair[1])

            if pair[1] not in list(adding_list.keys()):
                adding_list[pair[1]] = set()
            adding_list[pair[1]].add(pair[0])

    return adding_list


def edges_list_from_adjacency_list(adjacency_list: dict[int, set[int]]) -> list[tuple[int, int]]:
    edges_list = []
    for key in list(adjacency_list.keys()):
        for vertex in adjacency_list[key]:
            if (vertex, key) not in edges_list and (key, vertex) not in edges_list:
                edges_list.append((key, vertex))

    return edges_list


def graph_adding(graph: list[tuple[int, int]]) -> None:
    vertexes = vertex_list(graph)
    adding_list = create_adding_list(graph, vertexes)
    edges_list = edges_list_from_adjacency_list(adding_list)
    print(edges_list)