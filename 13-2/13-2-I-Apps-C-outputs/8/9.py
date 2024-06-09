
def solve(n, ranges):
    # Initialize the snow level at each point to 0
    snow_level = [0] * (n + 1)

    # Loop through each range and increment the snow level at each point in the range
    for a, b in ranges:
        for i in range(a, b + 1):
            snow_level[i] += 1

    # Initialize the number of ways to place the sensors to 0
    num_ways = 0

    # Loop through each point and check if it is a valid sensor placement
    for i in range(1, n + 1):
        if snow_level[i] > snow_level[i - 1] and snow_level[i] > snow_level[i + 1]:
            num_ways += 1

    return num_ways % 1000000009
