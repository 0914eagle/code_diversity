
def solve(n, x, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])
    
    # Initialize a queue to store the vertices to be processed
    queue = [x]
    visited = set()
    
    # Loop through the queue and find the shortest path from the starting vertex to the destination vertex
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == 1:
                return len(visited) - 1
            queue.extend(neighbors[vertex])
    
    # If the destination vertex is not found, return -1
    return -1

