
def solve(N, M, cubes):
    # Initialize a 2D array to represent the surface
    surface = [[0 for _ in range(N)] for _ in range(N)]

    # Place the cubes on the surface
    for r, c in cubes:
        surface[r-1][c-1] = 1

    # Initialize a queue to store the moves
    queue = []

    # Initialize the number of moves to 0
    moves = 0

    # Loop until the surface is filled with a rectangle
    while not is_rectangle(surface):
        # Find the topmost cube in each column
        top_cubes = [find_top_cube(surface, c) for c in range(N)]

        # Move the topmost cubes to the next row down
        for r, c in top_cubes:
            surface[r][c] = 0
            surface[r+1][c] = 1
            queue.append((r, c, r+1, c))

        # Increment the number of moves
        moves += 1

    # Return the number of moves
    return moves

# Check if the surface is filled with a rectangle
def is_rectangle(surface):
    # Check if the surface is filled with 1s
    if any(0 in row for row in surface):
        return False

    # Check if the surface is a rectangle
    for row in surface:
        if len(set(row)) != 1:
            return False

    return True

# Find the topmost cube in a column
def find_top_cube(surface, c):
    for r in range(len(surface)):
        if surface[r][c] == 1:
            return r, c

    return None

