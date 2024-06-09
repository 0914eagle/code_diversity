
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0] * N for _ in range(N)]

    # Place the cubes on the surface
    for cube in cubes:
        surface[cube[0] - 1][cube[1] - 1] = 1

    # Initialize a queue to store the coordinates of the cubes to be moved
    queue = []

    # Iterate through the surface and find the cubes that are not in the correct position
    for i in range(N):
        for j in range(N):
            if surface[i][j] == 1 and (i, j) != (N - 1, N - 1):
                queue.append((i, j))

    # Initialize a variable to store the number of moves
    moves = 0

    # Iterate through the queue and move the cubes to their correct position
    while queue:
        # Get the coordinates of the cube to be moved
        i, j = queue.pop(0)

        # Move the cube to the next square in the correct position
        surface[i][j] = 0
        surface[i + 1][j] = 1

        # Increment the number of moves
        moves += 1

    # Return the number of moves
    return moves

