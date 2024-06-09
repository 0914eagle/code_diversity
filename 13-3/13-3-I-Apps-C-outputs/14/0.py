
def solve(pulses):
    # Initialize a grid to store the activated pixels
    grid = [[0] * 200001 for _ in range(200001)]

    # Loop through each pulse
    for pulse in pulses:
        # Get the direction, starting time, length, and wire number of the pulse
        direction, start, length, wire = pulse

        # If the pulse is horizontal
        if direction == "h":
            # Loop through the length of the pulse
            for i in range(start, start + length):
                # Activate the pixels in the current row and the wire number
                for j in range(1, 200001):
                    grid[i][j] = 1
                    grid[i][wire] = 1
        # If the pulse is vertical
        else:
            # Loop through the length of the pulse
            for i in range(start, start + length):
                # Activate the pixels in the current column and the wire number
                for j in range(1, 200001):
                    grid[j][i] = 1
                    grid[wire][i] = 1

    # Count the number of activated pixels
    count = 0
    for i in range(1, 200001):
        for j in range(1, 200001):
            if grid[i][j] == 1:
                count += 1

    return count

