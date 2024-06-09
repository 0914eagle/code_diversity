
def count_ways(n):
    # Initialize a list to store the number of ways to split the stick
    ways = [0] * (n + 1)
    # Base case: if the stick is only one unit long, there is only one way to split it
    ways[1] = 1
    # Loop through all possible lengths of the first part
    for i in range(1, n):
        # Loop through all possible lengths of the second part
        for j in range(i, n):
            # If the sum of the lengths of the two parts is equal to the length of the stick,
            # then we can form a rectangle with these parts
            if i + j == n:
                # If the two parts have the same length, then we can form a square, so we only
                # consider cases where the two parts have different lengths
                if i != j:
                    # Add the number of ways to split the stick into four parts with the current
                    # lengths to the total number of ways
                    ways[n] += ways[i] * ways[j]
    return ways[n]

