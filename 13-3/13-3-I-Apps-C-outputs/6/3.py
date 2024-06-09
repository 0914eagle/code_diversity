
import sys

def get_distinct_routes(n, m, roads):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    # Find all possible routes using depth-first search
    routes = []
    for i in range(1, n + 1):
        route = [i]
        dfs(graph, route, i, n, routes)

    # Return the number of distinct routes
    return len(routes)

def dfs(graph, route, curr, n, routes):
    if len(route) == n:
        routes.append(route[:])
        return
    for neighbor in graph[curr]:
        if neighbor not in route:
            route.append(neighbor)
            dfs(graph, route, neighbor, n, routes)
            route.pop()

n, m = map(int, input().split())
roads = []
for _ in range(m):
    roads.append(list(map(int, input().split())))
print(get_distinct_routes(n, m, roads))

