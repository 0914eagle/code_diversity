
def solve(n, strengths):
    # Initialize a dictionary to store the teammate of each contestant
    teammates = {}
    
    # Iterate over the strengths of each possible team
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the strength of the team is higher than the current highest strength,
            # update the teammate of the first contestant in the team
            if strengths[i - 1][j - 1] > strengths[teammates[i] - 1][teammates[j] - 1]:
                teammates[i] = j
                teammates[j] = i
    
    # Return the teammate of each contestant
    return [teammates[i] for i in range(1, n + 1)]

