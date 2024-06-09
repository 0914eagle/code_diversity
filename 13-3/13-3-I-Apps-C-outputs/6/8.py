
import sys

def get_distinct_routes(n, m, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a-1].append(b-1)
    
    # Perform DFS to count the number of distinct routes
    visited = [False] * n
    count = 0
    def dfs(curr):
        nonlocal count
        visited[curr] = True
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                dfs(neighbor)
        count += 1
    
    dfs(0)
    return count

n, m = map(int, input().split())
roads = []
for _ in range(m):
    a, b = map(int, input().split())
    roads.append((a, b))

print(get_distinct_routes(n, m, roads))

