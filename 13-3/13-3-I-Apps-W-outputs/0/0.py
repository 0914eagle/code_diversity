
def find_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1 and iterate through the cycle
    curr_vertex = 1
    for i in range(l, r+1):
        # Add the current vertex to the cycle
        cycle.append(curr_vertex)
        
        # Find the next vertex in the cycle
        next_vertex = (curr_vertex % n) + 1
        
        # Update the current vertex
        curr_vertex = next_vertex
    
    # Return the lexicographically smallest cycle
    return cycle

