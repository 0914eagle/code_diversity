
def get_trail(program, grid):
    # Initialize the robot's location and the trail
    location = (0, 0)
    trail = [location]

    # Loop through the program
    for char in program:
        # Get the new location based on the character
        if char == "<":
            new_location = (location[0] - 1, location[1])
        elif char == ">":
            new_location = (location[0] + 1, location[1])
        elif char == "^":
            new_location = (location[0], location[1] - 1)
        elif char == "v":
            new_location = (location[0], location[1] + 1)

        # Check if the new location is valid
        if new_location[0] < 0 or new_location[0] >= len(grid) or new_location[1] < 0 or new_location[1] >= len(grid[0]):
            continue
        if grid[new_location[0]][new_location[1]] == "#":
            continue

        # Add the new location to the trail and update the location
        trail.append(new_location)
        location = new_location

    return trail

def get_repetition_length(trail):
    # Find the length of the trail
    length = len(trail)

    # Check if the trail is finite
    if length == 1:
        return 1

    # Find the smallest integer X such that the suffix of the trail will be a repetition of a continuous subsequence of the trail of length exactly X
    for x in range(2, length + 1):
        if trail[-x:] == trail[:x]:
            return x

    # If no such integer X exists, return 1
    return 1

if __name__ == '__main__':
    # Read the input
    N = int(input())
    program = input()
    grid = [input() for _ in range(N)]

    # Get the trail of the robot
    trail = get_trail(program, grid)

    # Find the repetition length of the trail
    repetition_length = get_repetition_length(trail)

    # Print the output
    print(repetition_length)

