
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0 for _ in range(N)] for _ in range(N)]

    # Place the cubes on the surface
    for cube in cubes:
        surface[cube[0] - 1][cube[1] - 1] = 1

    # Initialize a queue to store the coordinates of the cubes to be moved
    queue = []

    # Loop through the surface and find the coordinates of the cubes that are not in a rectangle
    for i in range(N):
        for j in range(N):
            if surface[i][j] == 1 and (i == 0 or j == 0 or i == N - 1 or j == N - 1):
                queue.append([i, j])

    # Initialize a variable to store the number of moves
    moves = 0

    # Loop through the queue and move the cubes to the rectangle
    while queue:
        # Get the coordinates of the cube to be moved
        i, j = queue.pop(0)

        # Find the coordinates of the square that the cube can be moved to
        for k in range(N):
            for l in range(N):
                if surface[k][l] == 0 and (k == 0 or l == 0 or k == N - 1 or l == N - 1):
                    # Move the cube to the square
                    surface[k][l] = 1
                    surface[i][j] = 0
                    moves += 1
                    break

    return moves

