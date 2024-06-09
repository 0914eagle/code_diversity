
def solve(n, m, a, b, roads):
    # Initialize a matrix to store the number of soldiers that should stay or move
    dp = [[0] * n for _ in range(n)]
    
    # Loop through each city
    for i in range(n):
        # If the city has no soldiers, skip it
        if a[i] == 0:
            continue
        
        # Loop through each neighboring city
        for j in range(n):
            # If the city has no soldiers or if it is the same city, skip it
            if a[j] == 0 or i == j:
                continue
            
            # If the number of soldiers in the city is greater than the number of soldiers that should be in the city,
            # then some soldiers need to move
            if a[i] > b[i]:
                # Calculate the number of soldiers that need to move
                num_soldiers = a[i] - b[i]
                
                # Update the number of soldiers that should move from the current city to the neighboring city
                dp[i][j] += num_soldiers
                
                # Update the number of soldiers that should move from the neighboring city to the current city
                dp[j][i] += num_soldiers
    
    # Check if the number of soldiers in each city is correct
    for i in range(n):
        if a[i] != b[i]:
            return "NO"
    
    # If all the conditions are met, return the matrix of soldiers that should stay or move
    return "YES\n" + "\n".join([" ".join(map(str, row)) for row in dp])

