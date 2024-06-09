
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

        # Check if the new location is passable
        if grid[new_location[0]][new_location[1]] == ".":
            # Add the new location to the trail
            trail.append(new_location)
            location = new_location

    return trail

def get_repetition_length(trail):
    # Find the length of the trail
    length = len(trail)

    # Check if the trail is finite
    if length == 1:
        return 1

    # Initialize the repetition length
    repetition_length = 1

    # Iterate through the trail
    for i in range(1, length):
        # Check if the suffix of the trail is a repetition of the trail
        if trail[i:] == trail[:length - i]:
            # Update the repetition length
            repetition_length = length - i
            break

    return repetition_length

def main():
    # Read the input
    N = int(input())
    program = input()
    grid = [input() for _ in range(N)]

    # Get the trail of the robot
    trail = get_trail(program, grid)

    # Get the repetition length of the trail
    repetition_length = get_repetition_length(trail)

    # Print the output
    print(repetition_length)

if __name__ == '__main__':
    main()

