
def solve(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1
    curr_vertex = 1
    
    # Iterate until we have visited all edges
    while len(cycle) < n * (n - 1) + 1:
        # If we have visited all vertices, start again from vertex 1
        if curr_vertex == n + 1:
            curr_vertex = 1
        
        # If we have not visited the current vertex before, add it to the cycle
        if curr_vertex not in cycle:
            cycle.append(curr_vertex)
        
        # Move to the next vertex
        curr_vertex += 1
    
    # Return the segment of the cycle specified by l and r
    return cycle[l-1:r]

