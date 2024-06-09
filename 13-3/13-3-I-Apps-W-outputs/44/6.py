
def solve_problem(n, m, c_l, c_e, v, queries):
    # Initialize a dictionary to store the shortest distance from each section to the elevator or stairs
    distances = {}
    
    # Loop through each section and calculate the shortest distance to the elevator or stairs
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:
                # If we are on the first floor, the shortest distance is zero
                distances[(i, j)] = 0
            elif j in l:
                # If we are on a stair, the shortest distance is the number of floors above the stair
                distances[(i, j)] = i - 1
            elif j in e:
                # If we are on an elevator, the shortest distance is the number of floors above the elevator
                distances[(i, j)] = i - 1
            else:
                # If we are on a regular section, the shortest distance is the minimum of the distances to the stairs and elevators
                distances[(i, j)] = min([distances[(i-1, k)] for k in l + e])
    
    # Loop through each query and calculate the shortest distance from the starting section to the finishing section
    results = []
    for query in queries:
        x1, y1, x2, y2 = query
        results.append(distances[(x1, y1)] + distances[(x2, y2)] + abs(x1 - x2))
    
    return results

