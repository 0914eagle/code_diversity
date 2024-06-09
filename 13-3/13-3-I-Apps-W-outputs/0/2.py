
def get_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1
    current_vertex = 1
    
    # Iterate until we have visited all edges
    while len(cycle) < n * (n - 1) + 1:
        # If the current vertex has not been visited, add it to the cycle
        if current_vertex not in cycle:
            cycle.append(current_vertex)
        
        # Find the next vertex to visit by looking for the first unvisited neighbor
        for neighbor in range(1, n + 1):
            if (current_vertex, neighbor) in edges and neighbor not in cycle:
                current_vertex = neighbor
                break
    
    # Return the segment of the cycle specified by l and r
    return cycle[l - 1:r]

