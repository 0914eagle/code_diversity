
def solve(n, strengths):
    # Initialize a dictionary to store the teammate of each person
    teammates = {}
    
    # Loop through each person and find their teammate
    for i in range(1, n+1):
        # Find the maximum strength of all possible teammates for person i
        max_strength = max([strengths[i][j] for j in range(1, n+1) if j != i])
        
        # Find the person with the maximum strength who is willing to be a teammate with person i
        teammate = [j for j in range(1, n+1) if strengths[i][j] == max_strength and j != i][0]
        
        # Add the teammate to the dictionary
        teammates[i] = teammate
    
    # Return the dictionary of teammates
    return teammates

