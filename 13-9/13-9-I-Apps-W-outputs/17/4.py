
def count_ways(n):
    # Initialize a list to store the number of ways for each length
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for length in range(1, n + 1):
        # Loop over the possible lengths of the parts
        for i in range(length):
            # Check if the length is not a square
            if length * length != i * i:
                # Add the number of ways for the current length to the total number of ways
                ways[length] += ways[i]
    
    return ways[n]

