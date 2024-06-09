
def find_min_path_sum(grid):
    # Initialize the minimum path sum to infinity
    min_path_sum = float('inf')
    # Initialize the current position as the top-left corner
    current_position = (0, 0)
    # Initialize the current minimum path sum as the value at the top-left corner
    current_min_path_sum = grid[0][0]

    # Loop through each position in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current position is the top-left corner, set the minimum path sum to its value
            if i == 0 and j == 0:
                min_path_sum = grid[i][j]
            # If the current position is not the top-left corner, check if the minimum path sum is less than the sum of the current position and its left and top neighbors
            else:
                # If the current position has a value less than the minimum path sum, set the minimum path sum to its value
                if grid[i][j] < min_path_sum:
                    min_path_sum = grid[i][j]
                # If the current position has a value equal to the minimum path sum, check if the sum of its left and top neighbors is less than the minimum path sum
                elif grid[i][j] == min_path_sum:
                    # If the sum of the current position and its left neighbor is less than the minimum path sum, set the minimum path sum to its value
                    if i > 0 and grid[i][j] + grid[i - 1][j] < min_path_sum:
                        min_path_sum = grid[i][j] + grid[i - 1][j]
                    # If the sum of the current position and its top neighbor is less than the minimum path sum, set the minimum path sum to its value
                    if j > 0 and grid[i][j] + grid[i][j - 1] < min_path_sum:
                        min_path_sum = grid[i][j] + grid[i][j - 1]

    return min_path_sum

