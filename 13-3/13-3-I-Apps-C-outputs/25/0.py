
def get_activated_pixels(pulses):
    # Initialize a grid to store the activated pixels
    grid = [[0] * 200001 for _ in range(200001)]

    # Iterate over the pulses and mark the activated pixels
    for pulse in pulses:
        direction, start, length, wire = pulse
        if direction == "h":
            for i in range(start, start + length):
                grid[i][wire] = 1
        else:
            for i in range(start, start + length):
                grid[wire][i] = 1

    # Count the number of activated pixels
    activated_pixels = 0
    for row in grid:
        for pixel in row:
            if pixel == 1:
                activated_pixels += 1

    return activated_pixels

if __name__ == '__main__':
    n = int(input())
    pulses = []
    for _ in range(n):
        direction, start, length, wire = input().split()
        pulses.append((direction, int(start), int(length), int(wire)))
    print(get_activated_pixels(pulses))

