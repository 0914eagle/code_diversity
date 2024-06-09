
import sys

def get_snow_levels(snow_log):
    snow_levels = []
    for a, b in snow_log:
        for i in range(a, b+1):
            if i not in snow_levels:
                snow_levels.append(i)
    return snow_levels

def get_number_of_ways(snow_log):
    snow_levels = get_snow_levels(snow_log)
    n = len(snow_levels)
    if n < 3:
        return 0
    ways = 1
    for i in range(n-2):
        ways *= (snow_levels[i+2] - snow_levels[i])
    return ways % 1000000009

n = int(input())
snow_log = []
for i in range(n):
    a, b = map(int, input().split())
    snow_log.append((a, b))
print(get_number_of_ways(snow_log))

