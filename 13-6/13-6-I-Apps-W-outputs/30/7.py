
def solve(n, heights):
    # Sort the heights in non-decreasing order
    sorted_heights = sorted(heights)
    # Initialize the minimum discomfort to a large value
    min_discomfort = float('inf')
    # Initialize the optimal order to an empty list
    optimal_order = []
    # Iterate over all possible starting points
    for i in range(n):
        # Calculate the discomfort of the circle with the current starting point
        discomfort = calculate_discomfort(sorted_heights, i)
        # If the discomfort is smaller than the minimum discomfort, update the minimum discomfort and the optimal order
        if discomfort < min_discomfort:
            min_discomfort = discomfort
            optimal_order = sorted_heights[i:i+n]
    return optimal_order

def calculate_discomfort(heights, start):
    # Calculate the absolute differences between adjacent heights in the circle
    absolute_differences = [abs(heights[i] - heights[(i+1)%len(heights)]) for i in range(len(heights))]
    # Return the sum of the absolute differences
    return sum(absolute_differences)

n = int(input())
heights = list(map(int, input().split()))
print(*solve(n, heights))

