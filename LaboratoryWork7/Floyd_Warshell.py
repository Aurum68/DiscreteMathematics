import networkx as nx
from datetime import datetime

inf = 10000000000

def prepare_matrix(graph: nx.Graph) -> list[list[float]]:
    matrix = [[inf]* len(graph.nodes) for _ in range(len(graph.nodes))]

    for i in range(len(graph.nodes)):
        for j in range(i, len(graph.nodes)):
            if i == j:
                matrix[i][j] = 0
            else:
                if (i, j) in graph.edges and not (j, i) in graph.edges:
                    matrix[i][j] = graph.edges[(i, j)]['weight']
                    matrix[j][i] = matrix[i][j]
                if (j, i) in graph.edges and not (i, j) in graph.edges:
                    matrix[j][i] = graph.edges[(j, i)]['weight']
                    matrix[i][j] = matrix[j][i]
                if (i, j) in graph.edges and (j, i) in graph.edges:
                    matrix[i][j] = graph.edges[(i, j)]['weight']
                    matrix[j][i] = matrix[i][j]
    return matrix


def floyd_warshall(graph: nx.Graph) -> list[list[float]]:
    matrix = prepare_matrix(graph)
    #parents = [[None for _ in range(len(graph.nodes))] for _ in range(len(graph.nodes))]

    start = datetime.now()
    long_time = False
    print(f"Starting Floyd Warshall...{len(graph.nodes)}: {start.strftime('%H:%M:%S')}")

    iterations = 0
    for k in range(len(matrix)):
        current_time = datetime.now()
        if current_time.timestamp() - start.timestamp() > 900:
            print(f"Current Floyd Warshall. {len(graph.nodes)}: {current_time.strftime('%H:%M:%S')}\n")
            long_time = True
            break
        for i in range(len(matrix)):

            for j in range(len(matrix)):
                iterations += 1
                # if inf > matrix[i][k] > -inf and inf > matrix[k][j] > -inf \
                #         and matrix[i][k] + matrix[k][j] < matrix[i][j]:
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    if long_time:
        return []
    print(f"Floyd Warshall iteration: {iterations}. Graph with {len(graph.nodes)} nodes and {len(graph.edges)} edges.")
    return matrix

