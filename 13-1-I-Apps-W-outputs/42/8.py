
def find_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1 and visit each vertex exactly once
    current_vertex = 1
    for i in range(n):
        # Add the current vertex to the cycle
        cycle.append(current_vertex)
        
        # Find the next vertex to visit by finding the unvisited neighbor of the current vertex
        # that is not equal to the current vertex
        next_vertex = 0
        for neighbor in graph[current_vertex]:
            if neighbor not in cycle:
                next_vertex = neighbor
                break
        
        # If there is no unvisited neighbor, then we have visited all vertices and can start again from vertex 1
        if next_vertex == 0:
            next_vertex = 1
        
        # Update the current vertex to the next vertex
        current_vertex = next_vertex
    
    # Return the segment of the cycle from l to r
    return cycle[l:r+1]

