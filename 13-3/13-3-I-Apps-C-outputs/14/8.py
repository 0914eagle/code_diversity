
def solve(pulses):
    # Initialize a grid to store the activation status of each pixel
    grid = [[0] * 200001 for _ in range(200001)]

    # Iterate over each pulse
    for pulse in pulses:
        # Extract the pulse information
        direction, start, length, wire = pulse

        # Determine the starting and ending coordinates of the pulse
        if direction == "h":
            start_x = wire
            start_y = 1
            end_x = wire + length - 1
            end_y = 200000
        else:
            start_x = 1
            start_y = wire
            end_x = 200000
            end_y = wire + length - 1

        # Iterate over the coordinates of the pulse
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                # If the pixel is not already activated, activate it
                if grid[x][y] == 0:
                    grid[x][y] = 1

    # Count the number of activated pixels
    count = 0
    for row in grid:
        count += sum(row)

    return count

