
def get_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1 and iterate through the vertices
    # in a clockwise direction
    curr_vertex = 1
    for i in range(n):
        # Add the current vertex to the cycle
        cycle.append(curr_vertex)
        
        # Find the next vertex to visit by finding the first vertex that
        # has not been visited yet and that is adjacent to the current vertex
        next_vertex = 1
        while next_vertex in cycle or next_vertex == curr_vertex:
            next_vertex += 1
        curr_vertex = next_vertex
    
    # Return the segment of the cycle specified by the input
    return cycle[l-1:r]

