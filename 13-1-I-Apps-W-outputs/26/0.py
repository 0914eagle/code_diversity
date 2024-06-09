
def solve(n, x, edges):
    # Create a graph object from the edges
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)
    # Initialize the distances from vertex 1 to all other vertices
    distances = {i: 0 for i in range(1, n + 1)}
    distances[1] = 1
    # Breadth-first search to find the shortest distance from vertex 1 to all other vertices
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    # Return the minimum distance from vertex x to vertex 1
    return distances[x]

