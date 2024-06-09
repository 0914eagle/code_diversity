
def is_harmonious(graph):
    n = len(graph)
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if graph[i][j] and graph[j][k] and not graph[i][k]:
                    return False
    return True

def add_edges(graph, m):
    n = len(graph)
    for i in range(n):
        for j in range(i+1, n):
            if not graph[i][j]:
                graph[i][j] = graph[j][i] = True
                m -= 1
                if m == 0:
                    return graph
    return graph

def solve(n, m, edges):
    graph = [[False for _ in range(n+1)] for _ in range(n+1)]
    for u, v in edges:
        graph[u][v] = graph[v][u] = True
    if is_harmonious(graph):
        return 0
    return m - add_edges(graph, m)

