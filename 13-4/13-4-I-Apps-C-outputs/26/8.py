
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

    # Initialize the current position and the set of visited positions
    current_row, current_col = start_row, start_col
    visited = set()

    # Initialize the minimum number of changes needed
    min_changes = 0

    # Iterate through the commands
    for command in commands:
        # Check if the current position is the goal position
        if current_row == goal_row and current_col == goal_col:
            break

        # Check if the current position is an obstacle
        if (current_row, current_col) in obstacles:
            # If the current position is an obstacle, skip the command
            min_changes += 1
            continue

        # Update the current position based on the command
        if command == "L":
            current_col -= 1
        elif command == "R":
            current_col += 1
        elif command == "U":
            current_row -= 1
        elif command == "D":
            current_row += 1

        # Add the current position to the set of visited positions
        visited.add((current_row, current_col))

    # Check if the goal position was reached
    if current_row == goal_row and current_col == goal_col:
        return min_changes

    # If the goal position was not reached, find the minimum number of changes needed to reach the goal
    min_changes += 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and (row, col) not in obstacles:
                min_changes += 1
                break

    return min_changes

