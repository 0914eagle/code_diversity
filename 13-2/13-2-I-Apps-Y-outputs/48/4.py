
def solve(columns, piece):
    # Initialize a list to store the heights of the columns
    heights = [0] * columns
    # Initialize a list to store the number of ways to drop the piece in each column
    ways = [0] * columns

    # Loop through each column and calculate the number of ways to drop the piece
    for i in range(columns):
        # If the piece is piece 1, 3, 5, or 7, it can be dropped in all columns
        if piece in [1, 3, 5, 7]:
            ways[i] = 1
        # If the piece is piece 2, 4, or 6, it can be dropped in all columns except the ones with height 0
        elif piece in [2, 4, 6]:
            ways[i] = 1 if heights[i] > 0 else 0
        # If the piece is piece 8, it can be dropped in all columns except the ones with height 0 or 1
        elif piece == 8:
            ways[i] = 1 if heights[i] > 1 else 0

    # Return the sum of the number of ways to drop the piece in each column
    return sum(ways)

