
def gl_bot(N, program, grid):
    # Initialize the robot's location and trail
    location = (N-1, N-1)
    trail = [location]

    # Loop through the program
    for char in program:
        # Get the new location based on the character
        if char == "<":
            new_location = (location[0]-1, location[1])
        elif char == ">":
            new_location = (location[0]+1, location[1])
        elif char == "^":
            new_location = (location[0], location[1]-1)
        elif char == "v":
            new_location = (location[0], location[1]+1)

        # Check if the new location is valid
        if grid[new_location[0]][new_location[1]] == ".":
            # Add the new location to the trail
            trail.append(new_location)
            location = new_location

    # Check if the trail is finite
    if len(trail) < N*N:
        return 1

    # Find the smallest integer X such that the suffix of the trail is a repetition of a continuous subsequence of the trail of length exactly X
    X = 1
    while X < len(trail):
        if trail[:X] == trail[len(trail)-X:]:
            break
        X += 1

    return X

