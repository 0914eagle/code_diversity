
def solve(n, m, a, b, roads):
    # Initialize a matrix to store the number of soldiers that should stay or move from one city to another
    dp = [[0] * n for _ in range(n)]
    
    # Initialize a set to store the cities that have already been visited
    visited = set()
    
    # Loop through each city and its neighbors
    for i in range(n):
        for j in range(n):
            # If the current city is not the same as the neighboring city and the neighboring city has not been visited yet
            if i != j and j not in visited:
                # Add the number of soldiers that should move from the current city to the neighboring city to the matrix
                dp[i][j] += 1
                
                # Add the neighboring city to the set of visited cities
                visited.add(j)
    
    # Check if the number of soldiers in each city is equal to the number of soldiers that should be in that city
    for i in range(n):
        if a[i] != sum(dp[i]):
            return "NO"
    
    # If all the conditions are met, return "YES" and the matrix of soldiers that should move from one city to another
    return "YES\n" + "\n".join([" ".join(map(str, row)) for row in dp])

