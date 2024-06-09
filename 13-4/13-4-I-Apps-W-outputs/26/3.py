
def get_maximum_desires(desires, K):
    # Initialize a 2D array to store the color of each square
    grid = [[0 for _ in range(K)] for _ in range(K)]

    # Iterate through the desires and update the grid accordingly
    for desire in desires:
        x, y, color = desire
        grid[x][y] = 1 if color == "B" else -1

    # Count the number of connected components of each color
    black_components = 0
    white_components = 0
    for i in range(K):
        for j in range(K):
            if grid[i][j] == 1:
                black_components += 1
            elif grid[i][j] == -1:
                white_components += 1

    # Return the maximum number of desires that can be satisfied
    return max(black_components, white_components)

