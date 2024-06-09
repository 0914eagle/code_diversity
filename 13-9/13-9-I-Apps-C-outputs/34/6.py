
def gl_bot(N, program, grid):
    # Initialize the robot's location and trail
    location = (N-1, N-1)
    trail = [location]

    # Loop through the program
    for char in program:
        # Move the robot in the current direction
        if char == "<":
            location = (location[0]-1, location[1])
        elif char == ">":
            location = (location[0]+1, location[1])
        elif char == "^":
            location = (location[0], location[1]-1)
        elif char == "v":
            location = (location[0], location[1]+1)

        # Add the new location to the trail
        trail.append(location)

        # If the new location is impassable, skip this movement
        if grid[location[0]][location[1]] == "#":
            continue

    # If the trail is of finite length, return 1
    if len(trail) < N*N:
        return 1

    # Otherwise, find the length of the repetition
    for i in range(N*N):
        if trail[i:] == trail[:N*N-i]:
            return i+1

    # If no repetition is found, return 1
    return 1

