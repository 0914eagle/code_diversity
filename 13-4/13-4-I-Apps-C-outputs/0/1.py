
def solve(grid, commands):
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

    # Initialize the robot's position and direction
    row, col = start_row, start_col
    direction = "R"

    # Iterate through the commands and move the robot accordingly
    for command in commands:
        # Check if the robot has reached the goal
        if row == goal_row and col == goal_col:
            break

        # Check if the robot has encountered an obstacle
        if (row, col) in obstacles:
            break

        # Move the robot in the current direction
        if command == "L":
            col -= 1
        elif command == "R":
            col += 1
        elif command == "U":
            row -= 1
        elif command == "D":
            row += 1

    # Return the minimum number of changes needed to fix the program
    return len(commands) - 1

