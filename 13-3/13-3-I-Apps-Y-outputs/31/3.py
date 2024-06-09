
import math

n = int(input())
a = list(map(int, input().split()))

# Sort the list of coordinates in ascending order
a.sort()

# Calculate the minimum distance by finding the maximum distance between any two coordinates
min_distance = max(a[-1] - a[0], sum(a) - a[-1])

print(min_distance)

