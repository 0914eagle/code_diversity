
def solve(grid, k):
    # Initialize the number of paths to 0
    paths = 0

    # Loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current cell is the last cell in the grid
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                # If the xor of the path sum is equal to k, increment the number of paths
                if xor_sum(grid, i, j) == k:
                    paths += 1
            # If the current cell is not the last cell in the grid, recursively call the function
            else:
                # If the current cell is not the last cell in the row, recursively call the function with the next cell in the row
                if j < len(grid[0]) - 1:
                    paths += solve(grid, k, i, j+1)
                # If the current cell is not the last cell in the column, recursively call the function with the next cell in the column
                if i < len(grid) - 1:
                    paths += solve(grid, k, i+1, j)

    return paths

# Function to calculate the xor sum of a path
def xor_sum(grid, i, j):
    # Initialize the xor sum to the current cell value
    xor_sum = grid[i][j]
    # Loop through the path
    for i in range(i):
        # Xor the current cell value with the previous cell value
        xor_sum ^= grid[i][j]
    return xor_sum

