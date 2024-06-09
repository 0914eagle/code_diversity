
import sys

def get_min_height_diff(heights, k):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the minimum height difference
    min_height_diff = float('inf')
    # Iterate over the first k elements
    for i in range(k):
        # Calculate the height difference between the current element and the next element
        height_diff = heights[i+1] - heights[i]
        # Update the minimum height difference
        min_height_diff = min(min_height_diff, height_diff)
    return min_height_diff

n, k = map(int, input().split())
heights = list(map(int, input().split()))
print(get_min_height_diff(heights, k))

