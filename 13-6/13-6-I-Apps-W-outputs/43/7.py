
def count_ways(n):
    # Initialize a list to store the number of ways to fill the parking lot
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Iterate over the number of successive cars of the same make
    for i in range(1, n + 1):
        # Iterate over the number of cars of each make
        for j in range(1, 5):
            # Check if the current combination is valid
            if i - j >= 0 and ways[i - j] > 0:
                # Add the current combination to the total number of ways
                ways[i] += ways[i - j]
    
    return ways[n]

