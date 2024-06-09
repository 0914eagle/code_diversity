
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
                score[i] += dfs(neighbor)
        return score[i]
    
    # Calculate the score of each connected component
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    # Calculate the maximum possible profit
    profit = 0
    for i in range(n):
        profit += a[i]
        profit -= abs(score[i])
    
    return profit

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    print(get_maximum_profit(n, m, a, b, u, v))

