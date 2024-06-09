
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0] * N for _ in range(N)]

    # Place the cubes on the surface
    for r, c in cubes:
        surface[r - 1][c - 1] = 1

    # Initialize a queue to store the coordinates of the cubes to be moved
    queue = []

    # Loop through the surface and find the coordinates of the cubes that are not in the rectangle
    for r in range(N):
        for c in range(N):
            if surface[r][c] == 1 and (r == 0 or surface[r - 1][c] == 0) and (c == 0 or surface[r][c - 1] == 0):
                queue.append((r, c))

    # Initialize a variable to store the number of moves
    moves = 0

    # Loop through the queue and move the cubes to the rectangle
    while queue:
        r, c = queue.pop(0)
        if r == 0 and c == 0:
            continue
        if r > 0 and surface[r - 1][c] == 0:
            surface[r - 1][c] = 1
            queue.append((r - 1, c))
        if c > 0 and surface[r][c - 1] == 0:
            surface[r][c - 1] = 1
            queue.append((r, c - 1))
        moves += 1

    return moves

