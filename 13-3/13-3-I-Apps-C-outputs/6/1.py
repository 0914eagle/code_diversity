
import sys

def get_distinct_routes(n, m, roads):
    # Initialize a graph with the given number of nodes and edges
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # Use a depth-first search to find all distinct routes
    visited = [False] * (n + 1)
    routes = 0
    for i in range(1, n + 1):
        if not visited[i]:
            routes += 1
            dfs(i, visited, graph)
    
    return routes

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

n, m = map(int, input().split())
roads = []
for _ in range(m):
    a, b = map(int, input().split())
    roads.append((a, b))

print(get_distinct_routes(n, m, roads))

