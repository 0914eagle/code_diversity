
def get_drained_water(height, width, map, device_position):
    # Initialize the total drained water to 0
    total_drained_water = 0

    # Get the device row and column indices
    device_row, device_col = device_position

    # Loop through the map grid
    for row in range(height):
        for col in range(width):
            # Check if the current cell is covered by water
            if map[row][col] < 0:
                # Calculate the distance between the current cell and the device
                distance = abs(row - device_row) + abs(col - device_col)

                # Check if the distance is within the range of the device
                if distance <= 1:
                    # Increment the total drained water by the water volume of the current cell
                    total_drained_water += abs(map[row][col])

    # Return the total drained water
    return total_drained_water

