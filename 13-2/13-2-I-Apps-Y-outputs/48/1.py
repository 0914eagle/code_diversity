
def solve(columns, piece):
    # Initialize a list to store the possible ways to drop the piece
    ways = []
    
    # Iterate over each column
    for i in range(columns):
        # Check if the piece can be dropped in the current column
        if piece[i] <= columns - i:
            # Add the current column to the list of possible ways to drop the piece
            ways.append(i)
    
    # Return the number of possible ways to drop the piece
    return len(ways)

