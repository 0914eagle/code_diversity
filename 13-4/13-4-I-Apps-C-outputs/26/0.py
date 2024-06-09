
def get_min_changes(grid, commands):
    # Initialize variables
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    obstacles = set()

    # Parse the grid and find the start and goal positions
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
        if command == "L":
            current_col -= 1
        elif command == "R":
            current_col += 1
        elif command == "U":
            current_row -= 1
        elif command == "D":
            current_row += 1

        # If the current position is an obstacle, skip the command
        if (current_row, current_col) in obstacles:
            continue

        # If the current position is the goal, break the loop
        if current_row == goal_row and current_col == goal_col:
            break

        # Increment the number of changes
        num_changes += 1

    # Return the minimum number of changes needed to reach the goal
    return num_changes

