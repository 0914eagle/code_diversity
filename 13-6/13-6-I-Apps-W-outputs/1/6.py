
def solve(n, x, edges):
    # Initialize a dictionary to store the distances from vertex 1 to each other vertex
    distances = {}
    for i in range(1, n+1):
        distances[i] = float('inf')
    distances[1] = 0
    
    # Breadth-first search to calculate the distances from vertex 1 to each other vertex
    queue = [1]
    while queue:
        current = queue.pop(0)
        for neighbor in edges[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    # Return the minimum distance from vertex x to vertex 1, which is the maximum distance Bob can travel
    return distances[x]

