
def solve(C, P, heights):
    # Initialize a list to store the number of ways to drop the piece in each column
    ways = [0] * C
    # Set the initial value for the first column to 1
    ways[0] = 1

    # Loop through each column
    for col in range(1, C):
        # Initialize a variable to store the number of ways to drop the piece in the current column
        total_ways = 0
        # Loop through each possible height for the current column
        for height in range(heights[col] + 1):
            # Check if the current height is valid for the current column
            if height <= heights[col]:
                # Add the number of ways to drop the piece in the previous column to the total number of ways
                total_ways += ways[col - 1]
        # Set the number of ways to drop the piece in the current column to the total number of ways
        ways[col] = total_ways

    # Return the number of ways to drop the piece in the last column
    return ways[C - 1]

