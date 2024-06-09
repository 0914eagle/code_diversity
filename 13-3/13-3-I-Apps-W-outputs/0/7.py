
def find_lexicographically_smallest_cycle(n, l, r):
    # Initialize a list to store the cycle
    cycle = []
    
    # Start at vertex 1 and iterate through the vertices
    for i in range(1, n + 1):
        # If the current vertex is in the range [l, r], add it to the cycle
        if l <= i <= r:
            cycle.append(i)
        # If the current vertex is the last vertex in the cycle, break
        if i == n:
            break
        # If the current vertex is not in the range [l, r], find the next vertex in the cycle
        else:
            # Find the next vertex in the cycle
            next_vertex = (i % n) + 1
            # If the next vertex is in the range [l, r], add it to the cycle
            if l <= next_vertex <= r:
                cycle.append(next_vertex)
    
    return cycle

