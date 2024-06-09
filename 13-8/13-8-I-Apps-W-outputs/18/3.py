
def solve(n, strength):
    # Initialize a dictionary to store the teammate of each contestant
    teammates = {}
    
    # Loop through each possible combination of two contestants
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the strength of the team is the highest so far, update the teammate of contestant i
            if strength[i][j] > strength[i][teammates.get(i, 0)]:
                teammates[i] = j
    
    # Return the teammate of each contestant
    return [teammates.get(i, 0) for i in range(1, n + 1)]

