
def solve(program, grid):
    # Initialize the robot's location and trail
    location = (0, 0)
    trail = [location]

    # Loop through the program
    for instruction in program:
        # Get the next location based on the instruction
        if instruction == "<":
            next_location = (location[0] - 1, location[1])
        elif instruction == ">":
            next_location = (location[0] + 1, location[1])
        elif instruction == "^":
            next_location = (location[0], location[1] - 1)
        elif instruction == "v":
            next_location = (location[0], location[1] + 1)

        # Check if the next location is valid
        if is_valid_location(next_location, grid):
            # Add the next location to the trail
            trail.append(next_location)
            # Update the robot's location
            location = next_location

    # Check if the trail is of finite length
    if len(trail) < 200:
        return 1

    # Find the length of the repetitive subsequence
    repetitions = 1
    for i in range(1, len(trail)):
        if trail[i] == trail[i - 1]:
            repetitions += 1
        else:
            break

    return repetitions

def is_valid_location(location, grid):
    # Check if the location is within the bounds of the grid
    if not (0 <= location[0] < len(grid) and 0 <= location[1] < len(grid[0])):
        return False
    # Check if the location is passable
    if grid[location[0]][location[1]] == "#":
        return False
    return True

