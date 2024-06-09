
def find_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1 and iterate through the cycle
    current_vertex = 1
    for i in range(l, r+1):
        # Add the current vertex to the cycle
        cycle.append(current_vertex)
        
        # Find the next vertex in the cycle
        next_vertex = find_next_vertex(current_vertex, n)
        
        # Update the current vertex
        current_vertex = next_vertex
    
    # Return the lexicographically smallest cycle
    return cycle

def find_next_vertex(current_vertex, n):
    # Find the next vertex in the cycle
    next_vertex = current_vertex + 1
    if next_vertex > n:
        next_vertex = 1
    
    # Return the next vertex
    return next_vertex

