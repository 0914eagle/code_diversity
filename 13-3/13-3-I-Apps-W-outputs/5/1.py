
def is_harmonious(graph):
    n = len(graph)
    for i in range(n):
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
                graph[i][j] = True
                m -= 1
                if m == 0:
                    return graph
    return graph

def solve(n, m, edges):
    graph = [[False for _ in range(n+1)] for _ in range(n+1)]
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u][v] = True
        graph[v][u] = True
    if is_harmonious(graph):
        return 0
    else:
        return add_edges(graph, m)

