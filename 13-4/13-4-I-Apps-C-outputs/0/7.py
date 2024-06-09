
def solve(grid, commands):
    # Initialize variables
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    obstacles = set()
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "S":
                start_row, start_col = row, col
            elif char == "G":
                goal_row, goal_col = row, col
            elif char == "#":
                obstacles.add((row, col))
    
    # Check if the start and goal positions are valid
    if start_row is None or start_col is None or goal_row is None or goal_col is None:
        return -1
    
    # Initialize the robot's position
    row, col = start_row, start_col
    
    # Initialize the number of changes needed
    changes_needed = 0
    
    # Iterate through the commands
    for command in commands:
        # Check if the command is valid
        if command not in ["L", "R", "U", "D"]:
            continue
        
        # Update the robot's position
        if command == "L":
            col -= 1
        elif command == "R":
            col += 1
        elif command == "U":
            row -= 1
        elif command == "D":
            row += 1
        
        # Check if the robot has reached the goal position
        if row == goal_row and col == goal_col:
            break
        
        # Check if the robot has hit an obstacle
        if (row, col) in obstacles:
            changes_needed += 1
            continue
    
    # Return the number of changes needed
    return changes_needed

