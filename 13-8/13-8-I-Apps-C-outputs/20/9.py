
def solve(altitudes, device_position):
    # Initialize the total volume of drained water to 0
    total_volume = 0

    # Get the height and width of the grid
    height, width = len(altitudes), len(altitudes[0])

    # Create a queue to store the positions of the cells to be processed
    queue = []

    # Add the position of the device to the queue
    queue.append(device_position)

    # Loop until the queue is empty
    while queue:
        # Get the current position from the queue
        i, j = queue.pop(0)

        # Check if the current position is a valid cell with negative altitude
        if 0 <= i < height and 0 <= j < width and altitudes[i][j] < 0:
            # Increment the total volume of drained water
            total_volume += abs(altitudes[i][j])

            # Set the altitude of the current cell to 0
            altitudes[i][j] = 0

            # Add the positions of the adjacent cells to the queue
            if i > 0:
                queue.append((i-1, j))
            if i < height-1:
                queue.append((i+1, j))
            if j > 0:
                queue.append((i, j-1))
            if j < width-1:
                queue.append((i, j+1))

    # Return the total volume of drained water
    return total_volume

