
def solve(n, m):
    # Initialize the number of non-similar worlds to 0
    non_similar_worlds = 0
    
    # Loop through each possible world
    for i in range(1, n+1):
        # Check if the world is non-similar to any of the previous worlds
        if i % (n-1) == 0:
            # Increment the number of non-similar worlds
            non_similar_worlds += 1
    
    # Return the number of non-similar worlds
    return non_similar_worlds % 1000000007

