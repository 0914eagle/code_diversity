
import sys

def get_snow_levels(n):
    snow_levels = []
    for i in range(n):
        a, b = map(int, input().split())
        snow_levels += list(range(a, b+1))
    return snow_levels

def count_ways(snow_levels):
    n = len(snow_levels)
    if n < 3:
        return 0
    snow_levels.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if snow_levels[i] < snow_levels[j] and snow_levels[j] < snow_levels[k]:
                    count += 1
    return count % 1000000009

n = int(input())
snow_levels = get_snow_levels(n)
print(count_ways(snow_levels))

