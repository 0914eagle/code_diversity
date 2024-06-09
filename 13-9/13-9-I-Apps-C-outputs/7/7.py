
def solve(n, m):
    # Initialize the number of non-similar worlds to 0
    non_similar_worlds = 0
    
    # Loop through each world
    for i in range(n):
        # Add the world to the number of non-similar worlds
        non_similar_worlds += 1
    
    # Return the number of non-similar worlds modulo 10^9 + 7
    return non_similar_worlds % (10**9 + 7)

