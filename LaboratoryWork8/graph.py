from collections import deque

class Graph:
    def __init__(self, vertices: int):
        self.V: int = vertices  # Количество вершин
        self.graph: list[list[int]] = [[0] * vertices for _ in range(vertices)]  # Матрица смежности для хранения графа
        self.flow: list[list[int]] = [[0] * vertices for _ in range(vertices)]  # Матрица смежности для хранения графа


    def add_edge(self, u, v, w):
        self.graph[u][v] = w  # Добавляем ребро с весом w
        self.flow[u][v] = w

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()

            for v in range(self.V):
                if not visited[v] and self.flow[u][v] > 0:  # Если вершина не посещена и есть остаточная емкость
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    if v == t:  # Если достигли целевой вершины
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V  # Массив для хранения пути
        max_flow = 0  # Инициализируем максимальный поток

        while self.bfs(source, sink, parent):
            # Находим минимальную емкость вдоль найденного пути
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.flow[parent[s]][s])
                s = parent[s]

            # Обновляем остаточные емкости рёбер и обратные рёбер
            v = sink
            while v != source:
                u = parent[v]
                self.flow[u][v] -= path_flow
                self.flow[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow  # Увеличиваем максимальный поток

        return max_flow

    def min_cut(self, source):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        # Находим все вершины, достижимые из источника
        while queue:
            u = queue.popleft()
            for v in range(self.V):
                if not visited[v] and self.flow[u][v] > 0:  # Остаточная емкость
                    queue.append(v)
                    visited[v] = True

        # Формируем минимальный разрез
        min_cut_edges = []
        for u in range(self.V):
            for v in range(self.V):
                if visited[u] and not visited[v] and self.flow[u][v] == 0 and self.graph[u][v] != 0:
                    min_cut_edges.append((u, v))

        cut_flow = 0
        for e in min_cut_edges:
            cut_flow += self.graph[e[0]][e[1]]
        return min_cut_edges, cut_flow

    def __str__(self) -> str:
        return str(self.graph)


letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

def create_graph(adjacency_list: dict[str, list[tuple[str, int]]]) -> Graph:
    global letters
    graph = Graph(len(adjacency_list))
    for node, edges in adjacency_list.items():
        for edge in edges:
            graph.add_edge(u=letters[node], v=letters[edge[0]], w=edge[1])
    return graph

def find_start(g: Graph) -> int:
    ends: set[str] = set()

    for i in range(g.V):
        for j in range(g.V):
            if i != j and g.graph[i][j] != 0:
                ends.add(list(letters.keys())[j])

    for node in range(g.V):
        if list(letters.keys())[node] not in ends:
            return node

    return -1

def find_end(g: Graph) -> int:
    starts: set[str] = set()

    for i in range(g.V):
        for j in range(g.V):
            if i != j and g.graph[i][j] != 0:
                starts.add(list(letters.keys())[i])

    for node in range(g.V):
        if list(letters.keys())[node] not in starts:
            return node

    return -1