
def solve(n, x, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a queue to store the vertices to be visited
    queue = [x]

    # Initialize a set to store the visited vertices
    visited = set()

    # Loop through the queue until it is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)

        # If the current vertex is the root vertex, return the number of moves
        if vertex == 1:
            return len(visited)

        # Add the current vertex to the visited set
        visited.add(vertex)

        # Add the neighbors of the current vertex to the queue
        for neighbor in neighbors[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

    # If the queue is empty, return the number of moves
    return len(visited)

