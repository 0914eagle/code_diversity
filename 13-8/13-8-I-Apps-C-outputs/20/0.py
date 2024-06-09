
def solve(height, width, grid, i, j):
    # Initialize the total volume of water drained to 0
    total_volume = 0

    # Loop through each row of the grid
    for row in range(height):
        # Loop through each column of the grid
        for col in range(width):
            # If the current cell has negative altitude (i.e., it is covered by water)
            if grid[row][col] < 0:
                # Calculate the distance from the current cell to the draining device
                distance = abs(row - i) + abs(col - j)

                # If the current cell is within the range of the device
                if distance <= 1:
                    # Add the volume of water in the current cell to the total volume
                    total_volume += abs(grid[row][col])

    # Return the total volume of water drained
    return total_volume

