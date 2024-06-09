
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
    def dfs(i, component_score):
        if visited[i]:
            return
        visited[i] = True
        component_score += b[i]
        for neighbor in graph[i]:
            component_score = dfs(neighbor, component_score)
        return component_score
    
    # Function to calculate the maximum profit
    def get_max_profit():
        max_profit = 0
        for i in range(n):
            if not visited[i]:
                score[i] = dfs(i, 0)
                max_profit = max(max_profit, score[i])
        return max_profit
    
    # Return the maximum profit
    return get_max_profit()

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    print(get_maximum_profit(n, m, a, b, u, v))

