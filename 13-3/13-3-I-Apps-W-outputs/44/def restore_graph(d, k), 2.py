
def restore_graph(d, k):
    n = len(d)
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        for j in range(i+1, n):
            if d[i] + d[j] <= k:
                graph[i].append(j)
                graph[j].append(i)
    m = 0
    for i in range(n):
        m += len(graph[i])
    return [m, graph]

