
import sys

def get_snow_levels(n):
    snow_levels = []
    for i in range(n):
        a, b = map(int, input().split())
        snow_levels += list(range(a, b + 1))
    return snow_levels

def count_ways(snow_levels):
    n = len(snow_levels)
    if n < 3:
        return 0
    snow_levels.sort()
    count = 0
    for i in range(n - 2):
        if snow_levels[i] < snow_levels[i + 1] and snow_levels[i + 1] < snow_levels[i + 2]:
            count += 1
    return count

n = int(input())
snow_levels = get_snow_levels(n)
result = count_ways(snow_levels)
print(result % 1000000009)

