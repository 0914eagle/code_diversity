
import sys

def solve(n, snow_log):
    # Initialize the number of ways to place the sensors as 0
    num_ways = 0

    # Sort the snow log by the starting point of the interval
    snow_log.sort(key=lambda x: x[0])

    # Initialize the current snow level as 0
    current_snow_level = 0

    # Loop through the snow log
    for i in range(n):
        # Get the current interval
        interval = snow_log[i]

        # Update the current snow level
        current_snow_level += interval[1] - interval[0] + 1

        # If the current snow level is greater than or equal to 3,
        # then we can place a sensor at this point
        if current_snow_level >= 3:
            num_ways += 1

            # Update the current snow level
            current_snow_level -= 3

    # If the current snow level is not 0, then we cannot place all three sensors
    if current_snow_level != 0:
        return "shovel time!"

    # Return the number of ways to place the sensors
    return num_ways % 1000000009

n = int(input())
snow_log = []

# Loop through the number of entries in the snow log
for i in range(n):
    # Get the current interval
    a, b = map(int, input().split())

    # Add the current interval to the snow log
    snow_log.append((a, b))

# Call the solve function and print the result
print(solve(n, snow_log))

