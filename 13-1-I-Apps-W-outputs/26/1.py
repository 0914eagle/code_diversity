
def solve(n, x, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])
    
    # Initialize a queue to store the vertices to be processed
    queue = [x]
    visited = set()
    
    # Loop through the vertices in the queue
    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)
        for neighbor in neighbors[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    # Return the number of vertices in the tree
    return len(visited)

