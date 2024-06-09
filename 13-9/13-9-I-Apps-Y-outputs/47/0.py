
def solve(n, a, edges):
    # Initialize a dictionary to store the distance of each vertex from the root
    distances = {}
    # Initialize a set to store the vertices that are already visited
    visited = set()
    # Choose the first vertex as the root
    root = 1
    # Initialize the maximum cost to 0
    max_cost = 0
    # Loop through all the vertices
    for i in range(1, n + 1):
        # If the vertex is not the root, calculate its distance from the root
        if i != root:
            # Initialize the distance to infinity
            distance = float('inf')
            # Loop through all the edges
            for edge in edges:
                # If the vertex is the destination of the edge and it has not been visited yet, calculate the distance
                if edge[1] == i and edge[0] not in visited:
                    # Calculate the distance as the sum of the distances from the root to the source of the edge and the distance from the source to the destination
                    distance = distances[edge[0]] + 1
                    # If the distance is less than the current distance, update the distance
                    if distance < distances.get(i, float('inf')):
                        distances[i] = distance
            # Add the vertex to the set of visited vertices
            visited.add(i)
        # Calculate the cost of the subtree with the current vertex as the root
        cost = sum([distances[i] * a[i] for i in distances])
        # If the cost is greater than the maximum cost, update the maximum cost
        if cost > max_cost:
            max_cost = cost
    # Return the maximum cost
    return max_cost

