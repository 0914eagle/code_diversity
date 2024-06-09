
def solve(state):
    # Initialize the number of moves as 0
    num_moves = 0
    # Loop through each row of the state
    for row in state:
        # Loop through each column of the row
        for col in row:
            # Check if the current cell is a dot
            if col == "*":
                # Increment the number of moves by 1
                num_moves += 1
                # Break out of the loop
                break
    # Return the number of moves
    return num_moves

