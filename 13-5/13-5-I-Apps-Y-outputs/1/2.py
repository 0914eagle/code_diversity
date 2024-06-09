
def read_data():
    n, m = map(int, input().split())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    queries = list(map(int, input().split()))
    return n, m, edges, queries

def build_graph(edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph

def dfs(graph, u, parent, dp, q):
    dp[u] = 1
    for v, w in graph[u]:
        if v != parent and w <= q:
            dfs(graph, v, u, dp, q)
            dp[u] += dp[v]

def solve(n, m, edges, queries):
    graph = build_graph(edges)
    dp = [0] * (n + 1)
    for q in queries:
        dfs(graph, 1, 0, dp, q)
        print(dp[1])

if __name__ == '__main__':
    n, m, edges, queries = read_data()
    solve(n, m, edges, queries)

