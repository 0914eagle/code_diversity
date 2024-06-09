
def min_separate_cities(n, m, roads):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
        graph[road[1] - 1].append(road[0] - 1)

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a variable to store the number of separate cities
    separate_cities = 0

    # Iterate through the graph
    for node in range(n):
        if node not in visited:
            # If the node is not visited, explore the node and mark it as visited
            explore_node(graph, node, visited)
            separate_cities += 1

    return separate_cities

def explore_node(graph, node, visited):
    # Mark the current node as visited
    visited.add(node)

    # Explore the neighbors of the current node
    for neighbor in graph[node]:
        if neighbor not in visited:
            explore_node(graph, neighbor, visited)

n, m = map(int, input().split())
roads = []
for _ in range(m):
    x, y = map(int, input().split())
    roads.append([x, y])

print(min_separate_cities(n, m, roads))

