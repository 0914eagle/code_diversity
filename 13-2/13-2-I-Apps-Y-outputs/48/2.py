
def solve(C, P, heights):
    # Initialize a list to store the number of ways to drop the piece in each column
    ways = [0] * C
    # Set the number of ways to drop the piece in the first column to 1
    ways[0] = 1
    # Loop through each column
    for col in range(1, C):
        # If the piece can be dropped in the current column
        if heights[col] >= P:
            # Add the number of ways to drop the piece in the previous column
            ways[col] += ways[col - 1]
        # If the piece cannot be dropped in the current column
        else:
            # Set the number of ways to drop the piece in the current column to 0
            ways[col] = 0
    # Return the sum of the number of ways to drop the piece in all columns
    return sum(ways)

