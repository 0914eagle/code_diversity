
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0] * N for _ in range(N)]

    # Place the cubes on the surface
    for r, c in cubes:
        surface[r-1][c-1] = 1

    # Initialize a queue to store the moves
    queue = []

    # Initialize a variable to store the number of moves
    moves = 0

    # Loop through the surface and find the rectangle
    for r in range(N):
        for c in range(N):
            # If the current square has a cube, add it to the queue
            if surface[r][c] == 1:
                queue.append((r, c))

    # Loop through the queue and make the moves
    while queue:
        # Get the current cube from the queue
        r, c = queue.pop(0)

        # Find the next square with a cube
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and surface[nr][nc] == 1:
                # Move the cube to the next square
                surface[nr][nc] = 0
                surface[r][c] = 1
                queue.append((nr, nc))
                moves += 1
                break

    return moves

