
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0] * N for _ in range(N)]

    # Populate the surface with the given cubes
    for r, c in cubes:
        surface[r - 1][c - 1] = 1

    # Initialize a queue to store the moves
    queue = []

    # Loop through each row of the surface
    for r in range(N):
        # Loop through each column of the surface
        for c in range(N):
            # If the current square has a cube on it
            if surface[r][c] == 1:
                # Add the move to the queue
                queue.append((r, c))

    # Initialize a variable to store the number of moves
    moves = 0

    # Loop through the queue
    while queue:
        # Pop the first move from the queue
        r, c = queue.pop(0)

        # Loop through the neighbors of the current square
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            # If the neighbor is within the bounds of the surface and has no cube on it
            if 0 <= nr < N and 0 <= nc < N and surface[nr][nc] == 0:
                # Move the cube to the neighbor
                surface[nr][nc] = 1
                surface[r][c] = 0

                # Add the move to the queue
                queue.append((nr, nc))

        # Increment the number of moves
        moves += 1

    # Return the number of moves
    return moves

