def minPath(grid, k):
    
    if not grid or not grid[0]:
        return []

    n = len(grid)
    m = len(grid[0])

    # Create a matrix of size n x m, filled with 0s
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    # Fill the matrix with the values from the grid
    for i in range(n):
        for j in range(m):
            matrix[i][j] = grid[i][j]

    # Fill the matrix with the values from the grid
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == n - 1 and j == m - 1:
                matrix[i][j] = k
            elif i == n - 1:
                matrix[i][j] = min(matrix[i + 1][j], matrix[i + 1][j + 1]) + matrix[i][j + 1]
            elif j == m - 1:
                matrix[i][j] = min(matrix[i][j + 1], matrix[i + 1][j]) + matrix[i + 1][j]
            else:
                matrix[i][j] = min(matrix[i][j + 1], matrix[i + 1][j]) + matrix[i + 1][j + 1]

    return matrix[0][0]


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    print(minPath(grid, k))
