
def count_paths(grid, k):
    # Initialize the number of paths to 0
    paths = 0

    # Loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is the destination cell, check if the xor sum is equal to k
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                if xor_sum(grid, i, j) == k:
                    paths += 1
            # If the current cell is not the destination cell, recursively call the function with the next cell
            else:
                if i < len(grid) - 1:
                    paths += count_paths(grid, k, i+1, j)
                if j < len(grid[0]) - 1:
                    paths += count_paths(grid, k, i, j+1)

    return paths

def xor_sum(grid, i, j):
    # Initialize the xor sum to the current cell value
    xor_sum = grid[i][j]

    # Loop through the previous cells and calculate the xor sum
    for x in range(i):
        for y in range(j):
            xor_sum ^= grid[x][y]

    return xor_sum

