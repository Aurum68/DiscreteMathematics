import itertools


def create_adjacency_list(graph: list[tuple[int, int]], vertex: list[int]) -> dict[int, set[int]]:
    adjacency_list = {}
    pairs = list(itertools.permutations(vertex, 2))
    for pair in pairs:
        if pair[0] == pair[1]:
            continue
        if pair in graph:
            if pair[0] not in list(adjacency_list.keys()):
                adjacency_list[pair[0]] = set()
            adjacency_list[pair[0]].add(pair[1])

            if pair[1] not in list(adjacency_list.keys()):
                adjacency_list[pair[1]] = set()
            adjacency_list[pair[1]].add(pair[0])
        else:
            if pair[0] not in list(adjacency_list.keys()):
                adjacency_list[pair[0]] = set()

            if pair[1] not in list(adjacency_list.keys()):
                adjacency_list[pair[1]] = set()

    return adjacency_list


def is_full(graph: list[tuple[int, int]], vertex: list[int]) -> bool:
    adjacency_list = create_adjacency_list(graph, vertex)
    for i in range(len(vertex) - 1):
        for j in range(i + 1, len(vertex)):
            if vertex[i] not in adjacency_list[vertex[j]]:
                return False
    return True


def vertex_list(graph: list[tuple[int, int]]) -> list[int]:
    return sorted(list(set([i[0] for i in graph] + [j[1] for j in graph])))


def max_full_subgraph(graph: list[tuple[int, int]]) -> None:
    vertexes = vertex_list(graph)
    for i in range(2, len(vertexes)):
        for vertex in list(itertools.combinations(vertexes, i)):
            if is_full(graph, list(vertex)):
                print(vertex)