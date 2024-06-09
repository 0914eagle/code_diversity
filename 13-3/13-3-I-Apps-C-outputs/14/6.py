
def solve(pulses):
    # Initialize a grid to store the activated pixels
    grid = [[0] * 200001 for _ in range(200001)]

    # Loop through each pulse
    for pulse in pulses:
        # Get the direction, starting time, length, and wire number of the pulse
        direction, start, length, wire = pulse

        # Determine the end time of the pulse
        end = start + length

        # Loop through the time range of the pulse
        for time in range(start, end):
            # Check if the pulse is horizontal or vertical
            if direction == "h":
                # Loop through the rows of the grid
                for row in range(200001):
                    # Check if the pulse is active in this row
                    if grid[row][time] == 0 and grid[row][wire] == 1:
                        # Activate the pixel in this row
                        grid[row][time] = 1
            else:
                # Loop through the columns of the grid
                for col in range(200001):
                    # Check if the pulse is active in this column
                    if grid[time][col] == 0 and grid[wire][col] == 1:
                        # Activate the pixel in this column
                        grid[time][col] = 1

    # Count the number of activated pixels
    count = 0
    for row in grid:
        for pixel in row:
            if pixel == 1:
                count += 1

    return count

