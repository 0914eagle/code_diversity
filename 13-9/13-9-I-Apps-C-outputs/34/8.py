
def solve(program, grid):
    # Initialize the robot's position and direction
    row, col = next((row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == "R")
    dir = 0

    # Initialize the trail as a list of tuples (row, col)
    trail = [(row, col)]

    # Loop through the program
    for char in program:
        # Update the direction based on the current character
        if char == "<":
            dir = (dir - 1) % 4
        elif char == ">":
            dir = (dir + 1) % 4

        # Update the position based on the direction
        if dir == 0:
            col -= 1
        elif dir == 1:
            row += 1
        elif dir == 2:
            col += 1
        elif dir == 3:
            row -= 1

        # Check if the new position is valid
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "#":
            break

        # Add the new position to the trail
        trail.append((row, col))

    # Check if the trail is of finite length
    if len(trail) < len(program):
        return 1

    # Find the smallest integer X such that the suffix of the trail has a repetition of a continuous subsequence of length X
    for x in range(1, len(trail)):
        if trail[-x:] == trail[:x]:
            return x

    # If no such integer exists, the trail is infinite
    return -1

