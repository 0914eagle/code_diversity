
def solve(n, x, edges):
    # Initialize a dictionary to store the distances from vertex 1 to each other vertex
    distances = {1: 0}
    for i in range(2, n + 1):
        distances[i] = float('inf')

    # Initialize a queue to do BFS
    queue = [1]

    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        current_vertex = queue.pop(0)

        # If the current vertex is the destination vertex, return the distance
        if current_vertex == x:
            return distances[current_vertex]

        # Get the neighbors of the current vertex
        neighbors = [edge[1] for edge in edges if edge[0] == current_vertex]

        # Loop through the neighbors and update the distances
        for neighbor in neighbors:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_vertex] + 1
                queue.append(neighbor)

    # If the destination vertex is not found, return -1
    return -1

