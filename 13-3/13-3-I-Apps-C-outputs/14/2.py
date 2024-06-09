
def solve(pulses):
    # Initialize a grid to store the activated pixels
    grid = [[0] * 200001 for _ in range(200001)]

    # Iterate over the pulses and activate the corresponding pixels
    for pulse in pulses:
        direction, start, length, wire = pulse
        if direction == "h":
            for i in range(start, start + length):
                grid[i][wire] = 1
        else:
            for i in range(start, start + length):
                grid[wire][i] = 1

    # Count the number of activated pixels
    count = 0
    for row in grid:
        for element in row:
            if element == 1:
                count += 1

    return count

