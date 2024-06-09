
def solve(columns, piece):
    # Initialize a list to store the number of ways to drop the piece in each column
    ways = [0] * columns

    # Set the initial height of the piece to be dropped
    height = piece

    # Iterate through each column
    for col in range(columns):
        # If the column is empty, set the number of ways to drop the piece to 1
        if height == 0:
            ways[col] = 1
        # If the column is not empty, set the number of ways to drop the piece to 0
        else:
            ways[col] = 0

    # Iterate through each column
    for col in range(columns):
        # If the column is not empty, iterate through each possible height
        if height > 0:
            for i in range(1, height + 1):
                # If the column is not empty and the piece can be dropped at the current height, set the number of ways to drop the piece to the sum of the current number of ways and the number of ways to drop the piece in the previous column
                if ways[col] > 0 and ways[col - 1] > 0:
                    ways[col] += ways[col - 1]

    # Return the number of ways to drop the piece in the last column
    return ways[-1]

