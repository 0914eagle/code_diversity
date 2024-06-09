
def solve(N, K, desires):
    # Initialize a 2D array to store the color of each square
    grid = [[0] * (K + 1) for _ in range(K + 1)]

    # Iterate over the desires and update the color of the corresponding square
    for x, y, c in desires:
        grid[x][y] = 1 if c == "B" else -1

    # Count the number of connected components of each color
    black_components = 0
    white_components = 0
    for i in range(K + 1):
        for j in range(K + 1):
            if grid[i][j] == 1:
                black_components += 1
            elif grid[i][j] == -1:
                white_components += 1

    # Return the maximum number of desires that can be satisfied
    return max(black_components, white_components)

