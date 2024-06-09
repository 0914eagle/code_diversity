
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0 for _ in range(N)] for _ in range(N)]

    # Place the cubes on the surface
    for cube in cubes:
        r, c = cube
        surface[r-1][c-1] = 1

    # Initialize a queue to store the moves
    queue = []

    # Initialize a variable to store the number of moves
    moves = 0

    # Loop through the surface and find the cube that is not in the rectangle
    for i in range(N):
        for j in range(N):
            if surface[i][j] == 1 and (i, j) not in queue:
                # Add the cube to the queue
                queue.append((i, j))
                break

    # Loop through the queue and make moves until the rectangle is formed
    while queue:
        # Get the first cube from the queue
        r, c = queue.pop(0)

        # Find the adjacent squares that are not in the rectangle
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i < N and 0 <= j < N and surface[i][j] == 0 and (i, j) not in queue:
                    # Add the adjacent square to the queue
                    queue.append((i, j))
                    # Update the surface
                    surface[i][j] = 1
                    moves += 1

    return moves

