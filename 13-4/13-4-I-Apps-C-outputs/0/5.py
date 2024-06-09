
def solve(grid, commands):
    # Initialize variables
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    obstacles = set()

    # Parse the grid and find the start and goal positions
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                goal_row, goal_col = row, col
            elif grid[row][col] == "#":
                obstacles.add((row, col))

    # Initialize the current position and commands
    current_row, current_col = start_row, start_col
    current_commands = commands

    # Loop through the commands and move the robot
    while current_commands:
        command = current_commands[0]
        if command == "L":
            current_col -= 1
        elif command == "R":
            current_col += 1
        elif command == "U":
            current_row -= 1
        elif command == "D":
            current_row += 1

        # Check if the robot has reached the goal
        if current_row == goal_row and current_col == goal_col:
            return len(commands) - len(current_commands)

        # Check if the robot has hit an obstacle
        if (current_row, current_col) in obstacles:
            return -1

        # Update the current commands
        current_commands = current_commands[1:]

    # If the robot has not reached the goal, return -1
    return -1

