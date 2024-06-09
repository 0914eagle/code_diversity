
def moves_until_score(state):
    # Convert the state to a 2D array
    array = [list(row) for row in state.split('\n')]
    
    # Initialize the number of moves as the total number of empty cells
    num_moves = sum(row.count('.') for row in array)
    
    # Iterate over each row
    for i in range(len(array)):
        # Iterate over each column
        for j in range(len(array[0])):
            # If the current cell is empty and there are no adjacent line segments, decrement the number of moves
            if array[i][j] == '.' and (i > 0 and array[i-1][j] in ('|', '-') or j > 0 and array[i][j-1] in ('|', '-')):
                num_moves -= 1
    
    return num_moves

