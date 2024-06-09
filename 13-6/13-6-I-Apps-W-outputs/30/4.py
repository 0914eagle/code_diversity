
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
            optimal_order = sorted_heights[:]
    # Return the optimal order
    return optimal_order

def calculate_discomfort(heights, start_index):
    # Calculate the discomfort of the circle with the given starting point
    discomfort = 0
    for i in range(len(heights)):
        # Calculate the absolute difference between the current and the next height
        diff = abs(heights[i] - heights[(i + start_index) % len(heights)])
        # Add the absolute difference to the total discomfort
        discomfort += diff
    # Return the total discomfort
    return discomfort

