
def find_min_separated_cities(n, m, roads):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
        graph[road[1] - 1].append(road[0] - 1)

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a variable to store the number of separated cities
    separated_cities = 0

    # Iterate through the graph
    for node in range(n):
        if node not in visited:
            # Explore the current node and its neighbors
            explore_node(graph, node, visited)
            separated_cities += 1

    return separated_cities

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
    roads.append(list(map(int, input().split())))

print(find_min_separated_cities(n, m, roads))

