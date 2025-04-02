from datetime import datetime, timedelta

import networkx as nx
from collections import namedtuple

inf = 10000000000
Edge = namedtuple("Edge", ("parent", "length"))

def prepare(graph: nx.Graph, start: int) -> dict[int, Edge]:
    matrix = dict()
    for node in graph.nodes:
        if node == start:
            matrix[node] = Edge(start, 0)
            continue
        matrix[node] = Edge(-1, inf)
    return matrix


def ford_bellman(graph: nx.Graph, start: int) -> dict[int, Edge]:
    matrix = prepare(graph, start)
    queue = [start]

    start_time = datetime.now()

    iterations = 0
    while queue:
        for edge in graph.edges:
            iterations += 1
            if queue[0] in edge:
                if queue[0] == edge[0]:
                    if graph.edges[edge]["weight"] + matrix[queue[0]].length < matrix[edge[1]].length:
                        matrix[edge[1]] = Edge(queue[0],
                                               graph.edges[edge]["weight"] + matrix[queue[0]].length)
                        queue.append(edge[1])
                if queue[0] == edge[1]:
                    if graph.edges[edge]["weight"] + matrix[queue[0]].length < matrix[edge[0]].length:
                        matrix[edge[0]] = Edge(queue[0],
                                                      graph.edges[edge]["weight"] + matrix[queue[0]].length)
                        queue.append(edge[0])
        queue.pop(0)
        current_time = datetime.now()
        if current_time - start_time > timedelta(minutes=15):
            return dict()

    print(f"Ford Bellman iterations: {iterations}. Graph with {len(graph.nodes)} nodes and {len(graph.edges)} edges.")
    return matrix