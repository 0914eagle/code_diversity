
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        graph[f[i]].append((i, w[i]))
    return graph

def dfs(graph, start, k, parent, weight, s, m):
    if k == 0:
        s[start] += weight
        m[start] = min(m[start], weight)
        return
    for i, w in graph[start]:
        if i != parent:
            dfs(graph, i, k-1, start, w, s, m)

def solve(n, k, f, w):
    graph = get_graph(n, f, w)
    s = [0] * n
    m = [float('inf')] * n
    for i in range(n):
        dfs(graph, i, k, -1, 0, s, m)
    return s, m

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    s, m = solve(n, k, f, w)
    for i in range(n):
        print(s[i], m[i])

if __name__ == '__main__':
    main()

