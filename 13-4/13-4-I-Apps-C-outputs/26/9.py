
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

    # Initialize the current position and the set of visited cells
    current_row, current_col = start_row, start_col
    visited = set()

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

        # If the current position is an obstacle or outside the grid, break the loop
        if (current_row, current_col) in obstacles or current_row < 0 or current_col < 0 or current_row >= len(grid) or current_col >= len(grid[0]):
            break

        # Add the current position to the set of visited cells
        visited.add((current_row, current_col))

        # If the current position is the goal, return the number of visited cells
        if current_row == goal_row and current_col == goal_col:
            return len(visited)

    # If the robot reached the end of the commands without reaching the goal, return -1
    return -1

