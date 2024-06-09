
import sys

n, k = map(int, input().split())
heights = sorted([int(input()) for _ in range(n)])

min_diff = float('inf')
for i in range(n - k + 1):
    diff = heights[i + k - 1] - heights[i]
    min_diff = min(min_diff, diff)

print(min_diff)

