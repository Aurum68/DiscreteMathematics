import math

import networkx as nx
import random


def add_k5(graph_loc: nx.Graph) -> list[int]:
    """Добавляет подграф K5 в граф."""
    k5_nodes = list(range(len(graph_loc), len(graph_loc) + 5))
    graph_loc.add_nodes_from(k5_nodes)

    # Полное соединение между K5
    for i in range(5):
        for j in range(i + 1, 5):
            # weight = math.floor(random.random() * random.choice([100, -100]))
            # graph_loc.add_edge(k5_nodes[i], k5_nodes[j], weight=
            #                    weight if weight != 0 else weight + random.choice([1, -1])
            # )

            weight = math.floor(random.random() * 100)
            graph_loc.add_edge(k5_nodes[i], k5_nodes[j],
                               weight=weight if weight != 0 else weight + 1)
    return k5_nodes


def add_k3_5(graph_loc: nx.Graph) -> tuple[list[int], list[int]]:
    """Добавляет подграф K3,5 в граф."""
    k3_nodes = list(range(len(graph_loc), len(graph_loc) + 3))
    k5_nodes = list(range(len(graph_loc) + 3, len(graph_loc) + 8))
    graph_loc.add_nodes_from(k3_nodes + k5_nodes)

    # Соединяем K3 с K5
    for k3_node in k3_nodes:
        for k5_node in k5_nodes:
            # weight = math.floor(random.random() * random.choice([100, -100]))
            # graph_loc.add_edge(k3_node, k5_node, weight=weight if weight != 0 else weight + random.choice([1, -1]))

            weight = math.floor(random.random() * 100)
            graph_loc.add_edge(k3_node, k5_node,
                               weight=weight if weight != 0 else weight + 1)
    return k3_nodes, k5_nodes


def create_graph(num_vertices: int) -> nx.Graph:
    """Создает связный граф с заданным числом вершин и добавляет K5 и K3,5."""
    if num_vertices < 10:
        raise ValueError("Число вершин должно быть не менее 10 для добавления K5 и K3,5.")

    graph_loc = nx.Graph()

    # Добавляем K5
    k5_nodes = add_k5(graph_loc)

    # Добавляем K3,5
    k35_3_nodes, k35_5_nodes = add_k3_5(graph_loc)

    # weight = math.floor(random.random() * random.choice([100, -100]))
    # graph_loc.add_edge(random.choice(k35_3_nodes), random.choice(k5_nodes),
    #                    weight=weight if weight != 0 else weight + random.choice([1, -1]))

    weight = math.floor(random.random() * 100)
    graph_loc.add_edge(random.choice(k35_3_nodes), random.choice(k5_nodes),
                        weight=weight if weight != 0 else weight + 1)
    # Добавляем оставшиеся вершины
    remaining_vertices = num_vertices - len(graph_loc.nodes)
    new_nodes = [i for i in range(num_vertices - remaining_vertices, num_vertices)]

    graph_loc.add_nodes_from(new_nodes)

    # Связываем оставшиеся вершины с существующими, чтобы граф был связным
    for node in range(len(graph_loc.nodes)):
        if node not in k5_nodes and node not in k35_3_nodes and node not in k35_5_nodes:
            # Соединяем со случайной вершиной из K5 или K3,5
            connect_to = random.choice(k5_nodes + k35_3_nodes + k35_5_nodes)
            # weight = math.floor(random.random() * random.choice([100, -100]))
            # graph_loc.add_edge(node, connect_to, weight=weight if weight != 0 else weight + random.choice([1, -1]))

            weight = math.floor(random.random() * 100)
            graph_loc.add_edge(node, connect_to, weight=weight if weight != 0 else weight + 1)

    return graph_loc