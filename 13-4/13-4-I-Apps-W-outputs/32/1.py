
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = [f[i], w[i]]
    return graph

def get_path(graph, k):
    s = 0
    m = float('inf')
    for i in range(k):
        s += graph[i][1]
        m = min(m, graph[i][1])
    return [s, m]

def solve(n, k, f, w):
    graph = get_graph(n, f, w)
    result = []
    for i in range(n):
        result.append(get_path(graph[i], k))
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    result = solve(n, k, f, w)
    for i in range(n):
        print(result[i][0], result[i][1])

