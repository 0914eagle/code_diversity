
def find_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1 and iterate through the cycle
    vertex = 1
    for i in range(l, r+1):
        # Add the current vertex to the cycle
        cycle.append(vertex)
        
        # Move to the next vertex in the cycle
        vertex = (vertex % n) + 1
    
    # Return the lexicographically smallest cycle
    return cycle

