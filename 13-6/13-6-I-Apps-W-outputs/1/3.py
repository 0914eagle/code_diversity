
def solve(n, x, edges):
    # Create a graph from the edges
    graph = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    # Initialize the distances from vertex 1 to all other vertices
    distances = [float('inf')] * (n + 1)
    distances[1] = 0
    # Breadth-first search from vertex 1 to find the shortest distance to all other vertices
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    # Return the minimum number of moves required for Alice to reach Bob
    return distances[x]

