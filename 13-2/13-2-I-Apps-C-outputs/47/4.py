
def f1(N, program, grid):
    # Initialize the robot's location and trail
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

        # Check if the new location is passable
        if grid[new_location[0]][new_location[1]] == ".":
            # Add the new location to the trail
            trail.append(new_location)
            # Update the robot's location
            location = new_location

    # Check if the trail is of finite length
    if len(trail) < N:
        return 1
    else:
        # Find the smallest integer X such that the suffix of the trail will be a repetition of a continuous subsequence of the trail of length exactly X
        X = 1
        while True:
            if trail[:X] == trail[len(trail) - X:]:
                break
            X += 1
        return X

def f2(N, program, grid):
    # Initialize the robot's location and trail
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

        # Check if the new location is passable
        if grid[new_location[0]][new_location[1]] == ".":
            # Add the new location to the trail
            trail.append(new_location)
            # Update the robot's location
            location = new_location

    # Check if the trail is of finite length
    if len(trail) < N:
        return 1
    else:
        # Find the smallest integer X such that the suffix of the trail will be a repetition of a continuous subsequence of the trail of length exactly X
        X = 1
        while True:
            if trail[:X] == trail[len(trail) - X:]:
                break
            X += 1
        return X

if __name__ == '__main__':
    N = int(input())
    program = input()
    grid = []
    for i in range(N):
        grid.append(list(input()))
    print(f1(N, program, grid))
    print(f2(N, program, grid))

