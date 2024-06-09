
def solve(n, p, k, improvements):
    # Initialize a graph to represent the pipes between the stations
    graph = [[] for _ in range(n + 1)]

    # Add the initial pipes to the graph
    for i in range(p):
        a, b, c = improvements[i]
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Initialize the maximum amount of water that can reach the mansion
    max_water = 0

    # Iterate over each improvement and calculate the maximum amount of water that can reach the mansion after each improvement
    for i in range(k):
        a, b, c = improvements[i + p]

        # If there is no pipe between a and b, create one with capacity c
        if not graph[a]:
            graph[a].append((b, c))
            graph[b].append((a, c))

        # Increase the capacity of the pipe between a and b by c
        for j, (neighbor, capacity) in enumerate(graph[a]):
            if neighbor == b:
                graph[a][j] = (neighbor, capacity + c)
                break

        # Calculate the maximum amount of water that can reach the mansion after the improvement
        max_water = max(max_water, dfs(graph, 1, n, {}))

    return [max_water] + [dfs(graph, 1, n, {}) for _ in range(k)]

# Depth-first search function to calculate the maximum amount of water that can reach the mansion from a given station
def dfs(graph, curr, target, visited):
    if curr == target:
        return 1000

    visited[curr] = True

    max_water = 0
    for neighbor, capacity in graph[curr]:
        if not visited[neighbor] and capacity > 0:
            max_water = max(max_water, dfs(graph, neighbor, target, visited))

    return max_water

