
def get_drained_water_volume(height, width, map_data, device_position):
    # Initialize the total drained water volume to 0
    total_volume = 0

    # Get the device position and altitude
    device_row, device_col = device_position
    device_altitude = map_data[device_row - 1][device_col - 1]

    # Loop through the map data and find all the cells that are connected to the device cell
    for row in range(height):
        for col in range(width):
            # If the current cell is connected to the device cell and has a negative altitude, add its volume to the total volume
            if map_data[row][col] < device_altitude and is_connected(map_data, row, col, device_row, device_col):
                total_volume += abs(map_data[row][col])

    # Return the total drained water volume
    return total_volume

# Check if two cells are connected
def is_connected(map_data, row1, col1, row2, col2):
    # Check if the cells are directly adjacent
    if row1 == row2 and abs(col1 - col2) == 1:
        return True
    if col1 == col2 and abs(row1 - row2) == 1:
        return True

    # Check if the cells are diagonally adjacent
    if abs(row1 - row2) == 1 and abs(col1 - col2) == 1:
        return True

    # If none of the above conditions are met, the cells are not connected
    return False

