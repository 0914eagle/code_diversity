
def count_activated_pixels(pulses):
    # Initialize a grid to store the state of each pixel
    grid = [[0] * 200001 for _ in range(200001)]

    # Iterate over the pulses and update the grid accordingly
    for pulse in pulses:
        direction, start, length, wire = pulse
        if direction == "h":
            for i in range(start, start + length):
                grid[i][wire] += 1
        else:
            for i in range(start, start + length):
                grid[wire][i] += 1

    # Count the number of activated pixels
    count = 0
    for row in grid:
        for pixel in row:
            if pixel == 2:
                count += 1

    return count

if __name__ == '__main__':
    n = int(input())
    pulses = []
    for _ in range(n):
        direction, start, length, wire = input().split()
        pulses.append((direction, int(start), int(length), int(wire)))
    print(count_activated_pixels(pulses))

