
def find_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1
    current_vertex = 1
    
    # Iterate until we have visited all edges
    while len(cycle) < n * (n - 1) + 1:
        # If we have visited all neighbors of the current vertex, move on to the next vertex
        if current_vertex not in cycle:
            # Add the current vertex to the cycle
            cycle.append(current_vertex)
            
            # Move to the next vertex
            current_vertex += 1
            
            # If we have reached the end of the cycle, move back to the beginning
            if current_vertex > n:
                current_vertex = 1
        else:
            # If we have already visited the current vertex, move on to the next vertex
            current_vertex += 1
    
    # Return the segment of the cycle specified by l and r
    return cycle[l:r+1]

