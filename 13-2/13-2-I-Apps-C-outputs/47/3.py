
def find_x(grid, program):
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

    # If the trail is of finite length, return 1
    if len(trail) < len(program):
        return 1

    # Otherwise, find the smallest integer X such that the suffix of the trail will be a repetition of a continuous subsequence of the trail of length exactly X
    for x in range(1, len(trail)):
        if trail[:x] * (len(trail) // x) == trail:
            return x

    # If no such integer X exists, return 0
    return 0

def main():
    grid_size = int(input())
    program = input()
    grid = []
    for _ in range(grid_size):
        grid.append(input())
    print(find_x(grid, program))

if __name__ == '__main__':
    main()

