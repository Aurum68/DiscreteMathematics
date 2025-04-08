import networkx as nx

def graph_to_bipartite(edges_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if is_graph_bipolar(edges_list):
        return edges_list

    # Создаем граф из списка рёбер
    graph = nx.Graph()
    graph.add_edges_from(edges_list)

    # Пытаемся раскрасить граф
    color = {}
    edges_to_remove = set()
    for node in graph.nodes():
        if node not in color:
            if not bfs_check_bipartite(graph, node, color):
                # Если граф не двудольный, ищем рёбра для удаления
                founded_edges = find_edges_to_remove(graph, color)
                for edge in founded_edges:
                    edges_to_remove.add(edge)

    new_edges = [edge for edge in edges_list if (edge[0], edge[1]) not in edges_to_remove
                 and (edge[1], edge[0]) not in edges_to_remove]
    return new_edges

def bfs_check_bipartite(graph: nx.Graph, start: int, color: dict) -> bool:
    queue = [start]
    color[start] = 0  # Начинаем с одного цвета

    while queue:
        node = queue.pop(0)
        for neighbor in graph.neighbors(node):
            if neighbor not in color:
                color[neighbor] = 1 - color[node]  # Присваиваем противоположный цвет
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                return False  # Найден конфликт, граф не двудольный

    return True

def find_edges_to_remove(graph: nx.Graph, color: dict) -> set:
    edges_to_remove = set()
    for u, v in graph.edges():
        if u in color and v in color:
            if color[u] == color[v]:
                edges_to_remove.add((u, v))
    return edges_to_remove

def is_graph_bipolar(edges_list: list[tuple[int, int]]) -> bool:
    graph = nx.Graph()
    graph.add_edges_from(edges_list)
    return nx.is_bipartite(graph)
