
def get_graph(n, k, f, w):
    graph = {}
    for i in range(n):
        graph[i] = {}
        for j in range(n):
            if f[i] == j:
                graph[i][j] = w[i]
    return graph

def dfs(graph, start, k, s, m):
    if k == 0:
        return s, m
    for i in graph[start]:
        if i not in s:
            s.add(i)
            m = min(m, graph[start][i])
            dfs(graph, i, k-1, s, m)
    return s, m

def solve(n, k, f, w):
    graph = get_graph(n, k, f, w)
    result = []
    for i in range(n):
        s, m = dfs(graph, i, k, set(), float('inf'))
        result.append((sum(graph[i][j] for j in s), min(graph[i][j] for j in s)))
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    result = solve(n, k, f, w)
    for i in range(n):
        print(result[i][0], result[i][1])

