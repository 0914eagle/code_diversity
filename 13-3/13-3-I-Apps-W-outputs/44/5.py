
def solve_world_programming_championship(n, m, c_l, c_e, v, queries):
    # Initialize a dictionary to store the shortest time to reach each section
    shortest_time = {}
    for i in range(1, n+1):
        for j in range(1, m+1):
            shortest_time[(i, j)] = float('inf')
    shortest_time[(1, 1)] = 0
    
    # Loop through each query
    for query in queries:
        x1, y1, x2, y2 = query
        # If the starting section is not the same as the finishing section, calculate the shortest time to reach the finishing section
        if (x1, y1) != (x2, y2):
            # If the finishing section is not on the same floor as the starting section, calculate the time to reach the finishing section on the same floor as the starting section
            if x1 != x2:
                # Calculate the time to reach the finishing section on the same floor as the starting section
                time = shortest_time[(x1, y1)] + abs(x1 - x2)
                # Update the shortest time to reach the finishing section if necessary
                if time < shortest_time[(x2, y2)]:
                    shortest_time[(x2, y2)] = time
            # If the finishing section is on the same floor as the starting section, calculate the time to reach the finishing section directly
            else:
                time = shortest_time[(x1, y1)] + abs(y1 - y2)
                # Update the shortest time to reach the finishing section if necessary
                if time < shortest_time[(x2, y2)]:
                    shortest_time[(x2, y2)] = time
    
    # Return the shortest time to reach each section
    return [shortest_time[(x, y)] for x, y in queries]

