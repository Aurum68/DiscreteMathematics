class GraphFord:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = [[0] * vertices for _ in range(vertices)]  # Матрица смежности

    def add_edge(self, u, v):
        self.graph[u][v] = 1  # Добавляем ребро из u в v

    def bfs(self, r_graph, s, t, parent):
        visited = [False] * self.V
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for v in range(self.V):
                if not visited[v] and r_graph[u][v] > 0:  # Если не посещена и есть остаточная емкость
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    if v == t:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        r_graph = [row[:] for row in self.graph]  # Копируем граф
        parent = [-1] * self.V  # Массив для хранения пути
        max_flow = 0  # Инициализируем максимальный поток

        while self.bfs(r_graph, source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, r_graph[parent[s]][s])
                s = parent[s]

            # Обновляем остаточную емкость рёбер и обратных рёбер
            v = sink
            while v != source:
                u = parent[v]
                r_graph[u][v] -= path_flow
                r_graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow, r_graph

    def find_matching_ford(self):
        # Предполагаем, что в графе есть source и sink
        source = 0
        sink = self.V - 1
        max_flow, r_graph = self.ford_fulkerson(source, sink)

        matching_edges = []
        for u in range(self.V):
            for v in range(self.V):
                if self.graph[u][v] == 1 and r_graph[v][u] == 1:
                    matching_edges.append((u, v))

        return max_flow, matching_edges




from collections import defaultdict


class GraphKhun:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.X = []
        self.Y = []
        self.used = defaultdict(bool)
        self.matching = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        if u not in self.X:
            self.X.append(u)
        if v not in self.Y:
            self.Y.append(v)

    def fill(self, dict_, value):
        for u in self.X:
            dict_[u] = value

    def find_matching_khun(self):
        self.matching = [-1] * self.V
        for u in self.X:
            self.fill(self.used, False)
            self.dfs(u)
        return self.matching

    def dfs(self, u):
        if self.used[u]:
            return False
        self.used[u] = True
        for v in self.graph[u]:
            if self.matching[v] == -1 or self.dfs(self.matching[v]):
                self.matching[v] = u
                return True
        return False


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __eq__(self, other):
        return self.u == other.v and self.v == other.u or self.u == other.u and self.v == other.v