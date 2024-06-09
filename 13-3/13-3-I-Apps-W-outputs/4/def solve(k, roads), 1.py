
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))

    # Find the shortest path between each pair of houses
    shortest_paths = {}
    for i in range(1, 2*k+1):
        for j in range(i+1, 2*k+1):
            shortest_paths[(i, j)] = find_shortest_path(graph, i, j)

    # Calculate the sum of the shortest paths for each pair of soulmates
    f = {i: 0 for i in range(1, k+1)}
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            f[i] += shortest_paths[(i, j)]

    # Return the minimum and maximum values of the sum of the shortest paths
    return min(f.values()), max(f.values())

def find_shortest_path(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == end:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            queue.append((neighbor, distance + weight))
    return 0

# Test case 1
k = 3
roads = [(1, 2, 3), (3, 2, 4), (2, 4, 3)]
print(solve(k, roads))

# Test case 2
k = 4
roads = [(1, 2, 1), (1, 3, 2), (1, 4, 3), (2, 4, 3), (3, 4, 2)]
print(solve(k, roads))

