
def solve(n, ranges):
    # Initialize the snow levels for each point
    snow_levels = [0] * (n + 1)

    # Loop through each range and update the snow levels
    for a, b in ranges:
        for i in range(a, b + 1):
            snow_levels[i] += 1

    # Initialize the number of ways to place the sensors
    num_ways = 0

    # Loop through each point and check if it is a valid sensor placement
    for i in range(1, n + 1):
        if snow_levels[i] > snow_levels[i - 1] and snow_levels[i] > snow_levels[i + 1]:
            num_ways += 1

    return num_ways % 1000000009

