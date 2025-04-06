import networkx as nx

def create_graph(adjacency_list: dict[str, list[tuple[str, int]]]) -> nx.DiGraph:
    graph = nx.DiGraph()
    for node, edges in adjacency_list.items():
        for edge in edges:
            if edge[1] != 0:
                graph.add_edge(node, edge[0], capacity=edge[1],)
    return graph


def find_start(graph: nx.DiGraph) -> str:
    ends: set[str] = set()

    for edge in graph.edges:
        ends.add(edge[1])

    for node in graph.nodes:
        if node not in ends:
            return node

    return ''


def find_end(graph: nx.DiGraph) -> str:
    starts: set[str] = set()

    for edge in graph.edges:
        starts.add(edge[0])

    for node in graph.nodes:
        if node not in starts:
            return node

    return ''