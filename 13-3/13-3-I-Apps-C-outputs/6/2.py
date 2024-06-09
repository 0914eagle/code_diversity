
import sys

def get_distinct_routes(n, m, roads):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    # Find all possible routes using a depth-first search
    routes = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            route = []
            dfs(i, graph, visited, route)
            routes.append(route)

    # Remove duplicates and return the number of distinct routes
    return len(set(map(frozenset, routes)))

def dfs(node, graph, visited, route):
    visited[node] = True
    route.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, route)
    return route

n, m = map(int, input().split())
roads = []
for _ in range(m):
    a, b = map(int, input().split())
    roads.append((a, b))
print(get_distinct_routes(n, m, roads))

