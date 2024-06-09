
def solve_problem(n, m, c_l, c_e, v, queries):
    # Initialize a dictionary to store the shortest distance from each section to the elevator or stairs
    distances = {}
    
    # Loop through each section and calculate the shortest distance to the elevator or stairs
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:
                # If we are on the first floor, the shortest distance to the elevator or stairs is zero
                distances[(i, j)] = 0
            elif i == n:
                # If we are on the last floor, the shortest distance to the elevator or stairs is the number of floors between the current floor and the first floor
                distances[(i, j)] = n - 1
            else:
                # If we are on any other floor, the shortest distance to the elevator or stairs is the minimum of the distances to the elevator or stairs on the previous floor plus one
                distances[(i, j)] = min(distances[(i-1, j)], distances[(i+1, j)]) + 1
    
    # Loop through each query and calculate the shortest distance from the starting section to the finishing section
    answers = []
    for query in queries:
        x1, y1, x2, y2 = query
        answers.append(distances[(x1, y1)] + distances[(x2, y2)] + abs(x1 - x2))
    
    return answers

