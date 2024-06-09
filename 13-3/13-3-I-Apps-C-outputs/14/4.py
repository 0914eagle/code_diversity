
def solve(pulses):
    # Initialize a grid to store the activated pixels
    grid = [[0] * 200001 for _ in range(200001)]

    # Loop through each pulse
    for pulse in pulses:
        # Get the direction, starting time, length, and wire number of the pulse
        direction, start, length, wire = pulse

        # Determine the end time of the pulse
        end = start + length

        # Loop through the grid rows/columns and activate the pixels that are intersected by the pulse
        for i in range(start, end):
            if direction == "h":
                for j in range(1, wire + 1):
                    grid[i][j] = 1
            else:
                for j in range(1, wire + 1):
                    grid[j][i] = 1

    # Count the number of activated pixels
    count = 0
    for i in range(1, 200001):
        for j in range(1, 200001):
            if grid[i][j] == 1:
                count += 1

    return count

