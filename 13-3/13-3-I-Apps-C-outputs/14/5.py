
def solve(pulses):
    # Initialize a grid to store the activation status of each pixel
    grid = [[0] * 200001 for _ in range(200001)]

    # Iterate over each pulse
    for pulse in pulses:
        # Extract the direction, starting time, length, and wire number of the pulse
        direction, start, length, wire = pulse

        # Determine the end time of the pulse
        end = start + length

        # Iterate over the time period when the pulse is active
        for time in range(start, end):
            # Determine the row and column of the pixel that is activated by the pulse
            if direction == "h":
                row = wire
                col = time
            else:
                row = time
                col = wire

            # Activate the pixel if it is not already activated
            if grid[row][col] == 0:
                grid[row][col] = 1

    # Count the number of activated pixels
    count = 0
    for row in grid:
        for pixel in row:
            if pixel == 1:
                count += 1

    return count

