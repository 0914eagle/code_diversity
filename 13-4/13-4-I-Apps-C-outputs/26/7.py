
def get_minimum_changes(grid, commands):
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

    # Initialize the current position and commands
    current_row, current_col = start_row, start_col
    current_commands = commands

    # Initialize the minimum number of changes
    min_changes = 0

    # Loop through the commands and update the current position
    for command in current_commands:
        # If the command is L, move left
        if command == "L":
            current_col -= 1
        # If the command is R, move right
        elif command == "R":
            current_col += 1
        # If the command is U, move up
        elif command == "U":
            current_row -= 1
        # If the command is D, move down
        elif command == "D":
            current_row += 1

        # If the current position is an obstacle, skip the command
        if (current_row, current_col) in obstacles:
            continue
        # If the current position is the goal, break the loop
        if current_row == goal_row and current_col == goal_col:
            break

        # Increment the minimum number of changes
        min_changes += 1

    # Return the minimum number of changes
    return min_changes

