
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0] * N for _ in range(N)]

    # Place the cubes on the surface
    for r, c in cubes:
        surface[r - 1][c - 1] = 1

    # Initialize a queue to store the positions of the cubes that need to be moved
    queue = []

    # Iterate through the surface and find the positions of the cubes that are not in the correct position
    for r in range(N):
        for c in range(N):
            if surface[r][c] == 1 and (r, c) != (1, 1):
                queue.append((r, c))

    # Initialize a variable to store the number of moves
    moves = 0

    # Iterate through the queue and move the cubes to the correct position
    while queue:
        r, c = queue.pop(0)
        surface[r][c] = 0
        surface[1][1] = 1
        moves += 1

    return moves

