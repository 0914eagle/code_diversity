
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
                graph[i][j] = graph[j][i] = 1
                m -= 1
                if m == 0:
                    return graph
    return graph

def solve(n, m, edges):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]][edge[1]] = graph[edge[1]][edge[0]] = 1
    if is_harmonious(graph):
        return 0
    else:
        return add_edges(graph, m)

