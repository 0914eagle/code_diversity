
def get_min_changes(grid, commands):
    # Initialize variables
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    obstacles = set()

    # Parse the grid and find the start, goal, and obstacles
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "S":
                start_row, start_col = row, col
            elif char == "G":
                goal_row, goal_col = row, col
            elif char == "#":
                obstacles.add((row, col))

    # Initialize the current position and the number of changes
    current_row, current_col = start_row, start_col
    num_changes = 0

    # Iterate through the commands and update the current position
    for command in commands:
        # Check if the command is valid and not blocked by an obstacle
        if command in ["L", "R", "U", "D"] and (current_row, current_col) not in obstacles:
            # Update the current position based on the command
            if command == "L":
                current_col -= 1
            elif command == "R":
                current_col += 1
            elif command == "U":
                current_row -= 1
            elif command == "D":
                current_row += 1

            # Check if the current position is the goal position
            if current_row == goal_row and current_col == goal_col:
                break

        # Increment the number of changes
        num_changes += 1

    # Return the minimum number of changes needed to reach the goal
    return num_changes

