
import sys

def solve(n, ranges):
    # Sort the ranges by their left endpoint
    ranges.sort(key=lambda x: x[0])

    # Initialize the snow level at each point to 0
    snow_level = [0] * (max(map(lambda x: x[1], ranges)) + 1)

    # Iterate through the ranges and update the snow level at each point
    for a, b in ranges:
        for i in range(a, b + 1):
            snow_level[i] += 1

    # Initialize the number of ways to place the sensors to 0
    num_ways = 0

    # Iterate through the points and check if they are valid for placing a sensor
    for i in range(1, len(snow_level)):
        if snow_level[i] > snow_level[i - 1] and snow_level[i] > snow_level[i + 1]:
            num_ways += 1

    return num_ways % 1000000009

n = int(input())
ranges = []
for i in range(n):
    a, b = map(int, input().split())
    ranges.append((a, b))

print(solve(n, ranges))

