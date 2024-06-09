
def solve(n, m, c_l, c_e, v, l, e, q, queries):
    # Initialize a dictionary to store the shortest time to reach each section
    shortest_time = {}
    for i in range(1, n+1):
        for j in range(1, m+1):
            shortest_time[(i, j)] = float('inf')
    shortest_time[(1, 1)] = 0
    
    # Loop through each query
    for query in queries:
        x1, y1, x2, y2 = query
        # If the starting section is not the same as the ending section, calculate the shortest time to reach the ending section
        if (x1, y1) != (x2, y2):
            # If the starting section is on a floor higher than the ending section, use the stairs to reach the ending section on the same floor
            if x1 > x2:
                for i in range(x1, x2-1, -1):
                    shortest_time[(i, y1)] = min(shortest_time[(i, y1)], shortest_time[(i+1, y1)] + 1)
            # If the starting section is on a floor lower than the ending section, use the stairs to reach the ending section on the same floor
            elif x1 < x2:
                for i in range(x1, x2+1):
                    shortest_time[(i, y1)] = min(shortest_time[(i, y1)], shortest_time[(i-1, y1)] + 1)
            # If the starting section is on the same floor as the ending section, use the elevator to reach the ending section on the same floor
            else:
                for i in range(1, m+1):
                    if i not in l and i not in e:
                        shortest_time[(x1, y1)] = min(shortest_time[(x1, y1)], shortest_time[(x1, i)] + 1)
    
    # Return the shortest time to reach each section
    return [shortest_time[(x2, y2)] for query in queries]

