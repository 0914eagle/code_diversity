
import sys

n, k = map(int, input().split())
heights = sorted(map(int, input().split()))

min_diff = float('inf')
for i in range(n - k + 1):
    max_height = heights[i + k - 1]
    min_height = heights[i]
    diff = max_height - min_height
    min_diff = min(min_diff, diff)

print(min_diff)

