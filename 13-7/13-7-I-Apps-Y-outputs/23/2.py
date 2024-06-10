
def get_new_state(state, move):
    # Initialize the new state with the current state
    new_state = state.copy()
    
    # Get the row and column indices of the non-zero elements in the state
    row_indices, col_indices = np.where(state != 0)
    
    # Determine the direction of the move
    if move == 0:  # left
        direction = (-1, 0)
    elif move == 1:  # up
        direction = (0, -1)
    elif move == 2:  # right
        direction = (1, 0)
    else:  # down
        direction = (0, 1)
    
    # Loop through the non-zero elements in the state and move them in the desired direction
    for i in range(len(row_indices)):
        row, col = row_indices[i], col_indices[i]
        new_row, new_col = row + direction[0], col + direction[1]
        
        # If the new position is out of bounds, wrap around to the other side of the grid
        if new_row < 0:
            new_row = 3
        elif new_row > 3:
            new_row = 0
        if new_col < 0:
            new_col = 3
        elif new_col > 3:
            new_col = 0
        
        # If the new position is empty, move the element to the new position
        if new_state[new_row, new_col] == 0:
            new_state[new_row, new_col] = state[row, col]
            new_state[row, col] = 0
    
    # Return the new state
    return new_state

def get_merged_state(state):
    # Initialize the merged state with the current state
    merged_state = state.copy()
    
    # Get the row and column indices of the non-zero elements in the state
    row_indices, col_indices = np.where(state != 0)
    
    # Loop through the non-zero elements in the state and merge them if they are adjacent and have the same value
    for i in range(len(row_indices)):
        row, col = row_indices[i], col_indices[i]
        value = state[row, col]
        
        # Check if the element is adjacent to another element with the same value
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 4 and 0 <= new_col < 4 and state[new_row, new_col] == value:
                merged_state[row, col] = 0
                merged_state[new_row, new_col] = value * 2
                break
    
    # Return the merged state
    return merged_state

def get_final_state(state, move):
    # Get the new state after the move
    new_state = get_new_state(state, move)
    
    # Get the merged state
    merged_state = get_merged_state(new_state)
    
    # Return the merged state
    return merged_state

if __name__ == '__main__':
    # Read the input state and move
    state = np.array(sys.stdin.read().split(), dtype=int).reshape(4, 4)
    move = int(input())
    
    # Get the final state
    final_state = get_final_state(state, move)
    
    # Print the final state
    print(final_state)

