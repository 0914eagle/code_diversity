
def rate_dance(grid):
    # Initialize variables
    rating = 0
    moves = 0

    # Loop through each row in the grid
    for row in grid:
        # Loop through each character in the row
        for i in range(len(row)):
            # Check if the current character is '$'
            if row[i] == '$':
                # Check if the previous character is not '$'
                if i > 0 and row[i-1] != '$':
                    # Increment the moves counter
                    moves += 1
            # Check if the current character is the last character in the row
            elif i == len(row) - 1:
                # Increment the moves counter
                moves += 1

    # Return the rating
    return moves

