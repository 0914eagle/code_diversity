
def f1(N, program, grid):
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

        # Check if the robot has reached the end of the grid
        if location[0] < 0 or location[0] >= N or location[1] < 0 or location[1] >= N:
            break

    # Check if the trail is of finite length
    if len(trail) == N * N:
        return 1

    # Find the smallest integer X such that the suffix of the trail will be a repetition of a continuous subsequence of the trail of length exactly X
    for X in range(2, N * N + 1):
        if trail[-X:] == trail[:X]:
            return X

    # If no such integer X exists, return -1
    return -1

def f2(N, program, grid):
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

        # Check if the robot has reached the end of the grid
        if location[0] < 0 or location[0] >= N or location[1] < 0 or location[1] >= N:
            break

    # Check if the trail is of finite length
    if len(trail) == N * N:
        return 1

    # Find the smallest integer X such that the suffix of the trail will be a repetition of a continuous subsequence of the trail of length exactly X
    for X in range(2, N * N + 1):
        if trail[-X:] == trail[:X]:
            return X

    # If no such integer X exists, return -1
    return -1

if __name__ == '__main__':
    N = int(input())
    program = input()
    grid = [input() for _ in range(N)]
    print(f1(N, program, grid))
    print(f2(N, program, grid))

