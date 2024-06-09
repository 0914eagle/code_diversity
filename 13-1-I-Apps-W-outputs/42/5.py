
def find_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1 and visit each vertex exactly once
    current_vertex = 1
    for i in range(n):
        # Add the current vertex to the cycle
        cycle.append(current_vertex)
        
        # Find the next vertex to visit by finding the unvisited neighbor of the current vertex
        # that is not the previous vertex
        next_vertex = 0
        for neighbor in range(1, n + 1):
            if neighbor != current_vertex and neighbor not in cycle:
                next_vertex = neighbor
                break
        
        # Update the current vertex and continue the loop
        current_vertex = next_vertex
    
    # Return the segment of the cycle specified by the input parameters
    return cycle[l:r]

