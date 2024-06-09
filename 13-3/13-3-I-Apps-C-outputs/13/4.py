
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
    def dfs(i, graph, visited, score):
        visited[i] = True
        for neighbor in graph[i]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, score)
        score[i] = abs(sum(b[i] for i in range(n) if visited[i]))
    
    # Function to calculate the maximum profit
    def get_max_profit(graph, a, b):
        max_profit = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, graph, visited, score)
                max_profit += score[i] - a[i]
        return max_profit
    
    return get_max_profit(graph, a, b)

