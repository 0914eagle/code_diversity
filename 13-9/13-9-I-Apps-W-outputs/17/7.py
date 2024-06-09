
def count_ways(n):
    # Initialize a list to store the number of ways to divide the stick
    ways = [0] * (n + 1)
    # Base case: if the length of the stick is 1, there is only one way to divide it
    ways[1] = 1
    # Loop through each length from 2 to n
    for length in range(2, n + 1):
        # Initialize a variable to store the number of ways to divide the stick into four parts
        num_ways = 0
        # Loop through each possible length for the first part
        for i in range(1, length):
            # If the first part has length i, the second part must have length length - i
            j = length - i
            # If the first part and the second part are not equal, they can form a rectangle
            if i != j:
                # Add the number of ways to divide the remaining stick into three parts
                num_ways += ways[length - i]
        # Add the number of ways to divide the current stick into four parts to the total number of ways
        ways[length] = num_ways
    # Return the number of ways to divide the stick into four parts that form a rectangle but not a square
    return ways[n]

