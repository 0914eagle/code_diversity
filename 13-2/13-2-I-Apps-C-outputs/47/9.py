
def get_trail(program, grid):
    # Initialize the robot's location and the trail
    location = (0, 0)
    trail = [location]

    # Iterate through the program
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

    # Find the smallest integer such that the suffix of the trail is a repetition of a continuous subsequence of the trail
    for i in range(1, length):
        if trail[:i] * (length // i) == trail:
            return i

    # If no such integer exists, return the length of the trail
    return length

if __name__ == '__main__':
    N = int(input())
    program = input()
    grid = [input() for _ in range(N)]
    trail = get_trail(program, grid)
    print(get_repetition_length(trail))

