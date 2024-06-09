
def get_min_changes(grid, commands):
    # Initialize variables
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    obstacles = set()

    # Parse the grid and find the start, goal, and obstacles
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                goal_row, goal_col = row, col
            elif grid[row][col] == "#":
                obstacles.add((row, col))

    # Initialize the minimum number of changes to infinity
    min_changes = float("inf")

    # Iterate over all possible commands
    for command in commands:
        # Initialize the current position and command index
        current_row, current_col = start_row, start_col
        command_index = 0

        # Iterate over the command string
        while command_index < len(commands):
            # Get the current command
            current_command = commands[command_index]

            # Check if the current command is valid
            if current_command in ["L", "R", "U", "D"]:
                # Move the current position based on the command
                if current_command == "L":
                    current_col -= 1
                elif current_command == "R":
                    current_col += 1
                elif current_command == "U":
                    current_row -= 1
                elif current_command == "D":
                    current_row += 1

                # Check if the new position is valid
                if (current_row, current_col) not in obstacles and 0 <= current_row < len(grid) and 0 <= current_col < len(grid[0]):
                    # If the new position is the goal, break the loop
                    if current_row == goal_row and current_col == goal_col:
                        break
                else:
                    # If the new position is not valid, break the loop
                    break
            else:
                # If the current command is not valid, break the loop
                break

            # Increment the command index
            command_index += 1

        # If the current position is the goal, update the minimum number of changes
        if current_row == goal_row and current_col == goal_col:
            min_changes = min(min_changes, command_index)

    # Return the minimum number of changes
    return min_changes

