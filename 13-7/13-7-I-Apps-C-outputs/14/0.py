
def dots_and_boxes(state):
    # Initialize variables
    n = len(state)
    rows, cols = n, n
    moves = 0
    points = 0

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is a dot, check if it is connected to any other dots
            if state[i][j] == '*':
                # Check if the dot is connected to the top dot
                if i > 0 and state[i-1][j] == '*':
                    points += 1
                # Check if the dot is connected to the bottom dot
                if i < rows-1 and state[i+1][j] == '*':
                    points += 1
                # Check if the dot is connected to the left dot
                if j > 0 and state[i][j-1] == '*':
                    points += 1
                # Check if the dot is connected to the right dot
                if j < cols-1 and state[i][j+1] == '*':
                    points += 1

    # Return the number of moves needed to score a point
    return moves + points

