
import sys

def get_distinct_routes(n, m, roads):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a list to store the routes
    routes = []

    # Recursive function to find all distinct routes
    def find_routes(curr_node, curr_route):
        # If the current node is the destination node, add the current route to the list of routes
        if curr_node == 2:
            routes.append(curr_route)
            return

        # If the current node has not been visited, mark it as visited and recurse on all its neighbors
        if curr_node not in visited:
            visited.add(curr_node)
            for neighbor in graph[curr_node]:
                find_routes(neighbor, curr_route + [neighbor])

    # Start the recursion from the starting node
    find_routes(1, [1])

    # Return the number of distinct routes
    return len(routes)

n, m = map(int, input().split())
roads = []
for _ in range(m):
    a, b = map(int, input().split())
    roads.append([a, b])

print(get_distinct_routes(n, m, roads))

