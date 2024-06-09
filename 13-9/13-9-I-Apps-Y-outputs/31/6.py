
def solve(n, m, roads):
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    result = []
    for i in range(1, n+1):
        result.append(len(graph[i]))
    return result

