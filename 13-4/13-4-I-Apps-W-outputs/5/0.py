
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            num_paths[(v, u)] = 1
            continue

        # If the query is for two different vertices, find the shortest path between them
        path = find_shortest_path(D, v, u)

        # If there is no path between the two vertices, the number of shortest paths is 0
        if not path:
            num_paths[(v, u)] = 0
            continue

        # If there is a path between the two vertices, find the number of shortest paths between them
        num_paths[(v, u)] = count_shortest_paths(path)

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] for v, u in queries]

def find_shortest_path(D, v, u):
    # Initialize a dictionary to store the shortest path between each pair of vertices
    shortest_path = {}

    # Initialize a queue to store the vertices to be processed
    queue = [(v, [v])]

    # Loop until the queue is empty
    while queue:
        # Get the current vertex and path from the queue
        vertex, path = queue.pop(0)

        # If the current vertex is the destination vertex, return the path
        if vertex == u:
            return path

        # If the current vertex is not the destination vertex, find the neighbors of the current vertex
        neighbors = get_neighbors(D, vertex)

        # Loop over the neighbors of the current vertex
        for neighbor in neighbors:
            # If the neighbor is not in the path, add it to the path and add it to the queue
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    # If there is no path between the two vertices, return an empty list
    return []

def get_neighbors(D, vertex):
    # Initialize a list to store the neighbors of the current vertex
    neighbors = []

    # Iterate over the divisors of the current vertex
    for divisor in range(1, int(math.sqrt(vertex)) + 1):
        # If the current divisor is a divisor of the current vertex, add it to the list of neighbors
        if vertex % divisor == 0:
            neighbors.append(divisor)

            # If the current divisor is not the only divisor of the current vertex, add the other divisor to the list of neighbors
            if divisor * divisor != vertex:
                neighbors.append(vertex // divisor)

    # Return the list of neighbors
    return neighbors

def count_shortest_paths(path):
    # Initialize a counter to store the number of shortest paths
    count = 0

    # Loop over the edges in the path
    for i in range(len(path) - 1):
        # Get the current edge and the next edge in the path
        edge = (path[i], path[i + 1])
        next_edge = (path[i + 1], path[i + 2])

        # If the current edge is not the same as the next edge, increment the counter
        if edge != next_edge:
            count += 1

    # Return the number of shortest paths
    return count

