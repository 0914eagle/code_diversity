
def find_trail_length(grid, program):
    # Initialize the robot's location and trail
    location = (0, 0)
    trail = [location]

    # Loop through the program
    for char in program:
        # Move the robot in the current direction
        if char == "<":
            location = (location[0] - 1, location[1])
        elif char == ">":
            location = (location[0] + 1, location[1])
        elif char == "^":
            location = (location[0], location[1] - 1)
        elif char == "v":
            location = (location[0], location[1] + 1)

        # Add the new location to the trail
        trail.append(location)

        # If the new location is impassable, skip this movement
        if grid[location[1]][location[0]] == "#":
            continue

    # Return the length of the trail
    return len(trail)

def main():
    # Read the input
    N = int(input())
    program = input()
    grid = []
    for _ in range(N):
        grid.append(input())

    # Find the trail length
    trail_length = find_trail_length(grid, program)

    # Print the output
    if trail_length == N:
        print(1)
    else:
        print(trail_length)

if __name__ == '__main__':
    main()

