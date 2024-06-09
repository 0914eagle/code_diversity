
def restore_graph(d, k):
    n = len(d)
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if d[i] + d[j] <= k:
                graph[i][j] = graph[j][i] = 1
    return graph

