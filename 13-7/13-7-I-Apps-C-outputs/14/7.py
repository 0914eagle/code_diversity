
def solve(state):
    # Initialize variables
    N = len(state)
    rows, cols = len(state[0]), len(state)
    moves = 0
    points = 0
    
    # Loop through each cell in the state
    for i in range(rows):
        for j in range(cols):
            # If the cell is a dot, check if it can be connected to any other dots
            if state[i][j] == '*':
                # Check if the dot can be connected to the dot above it
                if i > 0 and state[i-1][j] == '*':
                    state[i-1][j] = '|'
                    moves += 1
                # Check if the dot can be connected to the dot to the left of it
                if j > 0 and state[i][j-1] == '*':
                    state[i][j-1] = '-'
                    moves += 1
    
    # Loop through each cell in the state again
    for i in range(rows):
        for j in range(cols):
            # If the cell is a dot, check if it has been connected to all its neighbors
            if state[i][j] == '*':
                # Check if the dot has been connected to the dot above it
                if i > 0 and state[i-1][j] == '|':
                    points += 1
                # Check if the dot has been connected to the dot to the left of it
                if j > 0 and state[i][j-1] == '-':
                    points += 1
    
    # Return the number of moves that can be made before either Alice or Bob is guaranteed to have scored a point
    return moves + points

