
def get_min_changes(grid, commands):
    # Initialize variables
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    obstacles = set()
    for row, row_val in enumerate(grid):
        for col, col_val in enumerate(row_val):
            if col_val == "S":
                start_row, start_col = row, col
            elif col_val == "G":
                goal_row, goal_col = row, col
            elif col_val == "#":
                obstacles.add((row, col))
    
    # Check if the start and goal positions are valid
    if start_row is None or start_col is None or goal_row is None or goal_col is None:
        return -1
    
    # Initialize the current position and the set of visited positions
    current_row, current_col = start_row, start_col
    visited = set()
    
    # Initialize the minimum number of changes needed
    min_changes = 0
    
    # Iterate through the commands
    for command in commands:
        # Check if the current position is an obstacle
        if (current_row, current_col) in obstacles:
            return -1
        
        # Check if the current position is the goal position
        if current_row == goal_row and current_col == goal_col:
            break
        
        # Update the current position and the set of visited positions
        if command == "L":
            current_col -= 1
        elif command == "R":
            current_col += 1
        elif command == "U":
            current_row -= 1
        elif command == "D":
            current_row += 1
        visited.add((current_row, current_col))
        
        # Check if the current position has been visited before
        if (current_row, current_col) in visited:
            return -1
        
        # Increment the minimum number of changes needed
        min_changes += 1
    
    # Check if the goal position has been reached
    if current_row != goal_row or current_col != goal_col:
        return -1
    
    # Return the minimum number of changes needed
    return min_changes

