
def get_minimum_changes(grid, commands):
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
        raise ValueError("Invalid grid")

    # Initialize the current position and the number of changes
    current_row, current_col = start_row, start_col
    num_changes = 0

    # Iterate through the commands
    for command in commands:
        # Check if the command is valid
        if command not in ["L", "R", "U", "D"]:
            raise ValueError("Invalid command")

        # Update the current position based on the command
        if command == "L":
            current_col -= 1
        elif command == "R":
            current_col += 1
        elif command == "U":
            current_row -= 1
        elif command == "D":
            current_row += 1

        # Check if the current position is valid
        if (current_row, current_col) in obstacles:
            num_changes += 1
        elif current_row == goal_row and current_col == goal_col:
            break

    return num_changes

