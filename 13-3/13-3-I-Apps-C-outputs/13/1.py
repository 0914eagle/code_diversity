
def get_maximum_profit(n, m, a, b, u, v):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[u[i] - 1].append(v[i] - 1)
        graph[v[i] - 1].append(u[i] - 1)
    
    # Initialize a visited array and a score array
    visited = [False] * n
    score = [0] * n
    
    # Function to calculate the score of a connected component
    def dfs(i):
        if visited[i]:
            return
        visited[i] = True
        score[i] = b[i]
        for neighbor in graph[i]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    # Function to calculate the maximum profit
    def get_max_profit():
        max_profit = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                max_profit += abs(score[i])
        return max_profit - sum(a)
    
    return get_max_profit()

