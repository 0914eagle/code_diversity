
def solve(grid):
    # Initialize the shortest ladder length to 0
    shortest_ladder_length = 0

    # Loop through the grid from the north west corner to the south east corner
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If we find the special coin, return the shortest ladder length
            if grid[i][j] == 9:
                return shortest_ladder_length
            # If we are not at the south east corner, check the neighbors
            if i != len(grid) - 1 or j != len(grid[0]) - 1:
                # Check the north neighbor
                if i > 0 and grid[i - 1][j] != 0:
                    shortest_ladder_length = max(shortest_ladder_length, grid[i - 1][j])
                # Check the west neighbor
                if j > 0 and grid[i][j - 1] != 0:
                    shortest_ladder_length = max(shortest_ladder_length, grid[i][j - 1])
                # Check the south neighbor
                if i < len(grid) - 1 and grid[i + 1][j] != 0:
                    shortest_ladder_length = max(shortest_ladder_length, grid[i + 1][j])
                # Check the east neighbor
                if j < len(grid[0]) - 1 and grid[i][j + 1] != 0:
                    shortest_ladder_length = max(shortest_ladder_length, grid[i][j + 1])

    # If we reach this point, the special coin was not found, so return -1
    return -1

