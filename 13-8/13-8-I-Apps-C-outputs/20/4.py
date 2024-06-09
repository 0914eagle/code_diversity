
def solve(height, width, altitudes, i, j):
    # Initialize the total volume of water drained to 0
    total_volume = 0

    # Loop through each row of the grid
    for row in range(height):
        # Loop through each column of the grid
        for col in range(width):
            # Check if the current cell is a water cell (i.e., has negative altitude)
            if altitudes[row][col] < 0:
                # Calculate the volume of water in the current cell
                volume = abs(altitudes[row][col])

                # Check if the current cell is the cell where the draining device is placed
                if row == i and col == j:
                    # If the device is placed in a water cell, add the volume to the total volume
                    total_volume += volume
                else:
                    # If the device is not placed in a water cell, check if the cell is connected to the device through water flow
                    for neighbor in [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]:
                        # Check if the neighboring cell is a water cell and the device is not placed in that cell
                        if 0 <= neighbor[0] < height and 0 <= neighbor[1] < width and altitudes[neighbor[0]][neighbor[1]] < 0 and (neighbor[0] != i or neighbor[1] != j):
                            # If the cell is connected to the device through water flow, add the volume to the total volume
                            total_volume += volume

                            # Break out of the loop, as the cell is now drained and cannot be drained again
                            break

    # Return the total volume of water drained
    return total_volume

