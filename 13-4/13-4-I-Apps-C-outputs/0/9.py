
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

    # Initialize the current position and direction
    current_row, current_col = start_row, start_col
    direction = 0 # 0 = right, 1 = down, 2 = left, 3 = up

    # Iterate through the commands and move the robot
    for command in commands:
        # Check if the command is valid
        if command == "L":
            direction = (direction - 1) % 4
        elif command == "R":
            direction = (direction + 1) % 4
        elif command == "U":
            direction = (direction - 2) % 4
        elif command == "D":
            direction = (direction + 2) % 4

        # Move the robot in the current direction
        if direction == 0: # right
            current_col += 1
        elif direction == 1: # down
            current_row += 1
        elif direction == 2: # left
            current_col -= 1
        elif direction == 3: # up
            current_row -= 1

        # Check if the robot has reached the goal
        if current_row == goal_row and current_col == goal_col:
            return "Success"

        # Check if the robot has hit an obstacle
        if (current_row, current_col) in obstacles:
            return "Obstacle"

    # If the robot has not reached the goal, return failure
    return "Failure"

