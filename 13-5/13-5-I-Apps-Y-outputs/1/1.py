
def f1(n, m, edges, queries):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # DFS to find the shortest path between every pair of vertices
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j[0]] = j[1]

    # DP to find the maximum weight of an edge on a simple path between every pair of vertices
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][k] + dp[k][j] for k in range(1, n + 1) if dist[i][k] + dist[k][j] <= queries[i - 1])

    # Count the number of pairs of vertices with maximum weight less than or equal to the query
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if dp[i][j] <= queries[i - 1]:
                count += 1

    return count

def f2(n, m, edges, queries):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # DFS to find the shortest path between every pair of vertices
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j[0]] = j[1]

    # DP to find the maximum weight of an edge on a simple path between every pair of vertices
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][k] + dp[k][j] for k in range(1, n + 1) if dist[i][k] + dist[k][j] <= queries[i - 1])

    # Count the number of pairs of vertices with maximum weight less than or equal to the query
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if dp[i][j] <= queries[i - 1]:
                count += 1

    return count

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    queries = list(map(int, input().split()))
    print(f1(n, m, edges, queries))
    print(f2(n, m, edges, queries))

