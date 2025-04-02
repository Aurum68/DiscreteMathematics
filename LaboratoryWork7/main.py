from prepare_graph import *
from Floyd_Warshell import *
from Ford_Bellman import *


def output_floyd_warshall(matrix: list[list[float]], filename: str) -> None:
    with open(filename, "w") as file:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                file.write(str(matrix[i][j]) + " ")
            file.write("\n")


def output_ford_bellman(matrix: dict[int, Edge], filename: str) -> None:
    with open(filename, "w") as file:
        for node, edge in matrix.items():
            if edge.length == 0:
                file.write(f"{str(node)} = start: \n")
        for node, edge in matrix.items():
            if edge.length != 0:
                file.write(f"{str(node)}: {str(edge.length)}. It from {edge.parent}\n")


if __name__ == '__main__':
    vertex_counts = [500, 1500, 4500, 13500, 31000]
    graphs = {}

    for count in vertex_counts:
        graphs[count] = create_graph(count)

    # Вывод информации о графах
    for count, graph in graphs.items():
        with open(f"graph_{str(count)}.txt", "w") as file:
            for edge in graph.edges:
                file.write(f"edge: {edge}, weight: {graph.edges[edge]['weight']}\n")

    for count, graph in graphs.items():
        print('new')
        floyd_warshall_matrix = floyd_warshall(graph)
        if not floyd_warshall_matrix:
            print(f"Floyd Warshall. More than 15 minutes. Graph with {count} nodes.")
            continue
        output_floyd_warshall(floyd_warshall_matrix, f"floyd_warshall_{count}.txt")

    for count, graph in graphs.items():
        ford_bellman_matrix = ford_bellman(graph, 0)
        if ford_bellman_matrix == dict():
            print(f"Ford Bellman. More than 15 minutes. Graph with {count} nodes.")
            continue
        output_ford_bellman(ford_bellman_matrix, f"ford_bellman_{count}")

