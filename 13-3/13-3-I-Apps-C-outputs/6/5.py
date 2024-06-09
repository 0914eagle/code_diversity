
def num_routes(N, M, roads):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    # Find all possible routes using a depth-first search
    routes = []
    for i in range(1, N + 1):
        for route in dfs(graph, i, []):
            routes.append(route)

    # Return the number of distinct routes
    return len(set(routes))

def dfs(graph, node, route):
    # Add the current node to the route
    route.append(node)

    # If we have reached the end of the route, yield the route
    if node == N:
        yield route

    # Recursively search for routes from the current node
    for neighbor in graph[node]:
        if neighbor not in route:
            yield from dfs(graph, neighbor, route)

    # Backtrack and remove the current node from the route
    route.pop()

