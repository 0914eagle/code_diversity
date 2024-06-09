
def solve(altitudes, device_position):
    # Initialize the total volume of water drained to 0
    total_volume = 0

    # Get the height and width of the map
    height, width = len(altitudes), len(altitudes[0])

    # Iterate through each row of the map
    for i in range(height):
        # Iterate through each column of the map
        for j in range(width):
            # Check if the current cell is not land and is not the device position
            if altitudes[i][j] < 0 and (i, j) != device_position:
                # Calculate the distance between the current cell and the device position
                distance = abs(i - device_position[0]) + abs(j - device_position[1])

                # Add the water volume of the current cell to the total volume
                total_volume += altitudes[i][j] * distance

    # Return the total volume of water drained
    return total_volume

