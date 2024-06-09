
def get_min_changes(grid, command_string):
    # Initialize variables
    start_position = None
    goal_position = None
    obstacles = []

    # Parse the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":
                start_position = (row, col)
            elif grid[row][col] == "G":
                goal_position = (row, col)
            elif grid[row][col] == "#":
                obstacles.append((row, col))

    # Initialize the command string
    current_position = start_position
    commands = command_string.split()

    # Iterate through the commands
    for command in commands:
        # Check if the command is valid
        if command == "L":
            new_position = (current_position[0], current_position[1] - 1)
        elif command == "R":
            new_position = (current_position[0], current_position[1] + 1)
        elif command == "U":
            new_position = (current_position[0] - 1, current_position[1])
        elif command == "D":
            new_position = (current_position[0] + 1, current_position[1])
        else:
            continue

        # Check if the new position is valid
        if new_position in obstacles:
            continue

        # Update the current position
        current_position = new_position

        # Check if the goal has been reached
        if current_position == goal_position:
            break

    # Return the minimum number of changes needed
    return len(commands) - len(command_string.split())

