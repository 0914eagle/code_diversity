
def get_min_discomfort_circle(heights):
    n = len(heights)
    # Sort the heights in non-decreasing order
    sorted_heights = sorted(heights)
    # Initialize the minimum discomfort to a large value
    min_discomfort = float('inf')
    # Initialize the optimal ordering to an empty list
    optimal_ordering = []
    # Iterate over all possible start points
    for start in range(n):
        # Initialize the current discomfort to 0
        current_discomfort = 0
        # Iterate over all elements in the circle
        for i in range(n):
            # Calculate the absolute difference between the current and next height
            absolute_difference = abs(sorted_heights[i] - sorted_heights[(i + start) % n])
            # Add the absolute difference to the current discomfort
            current_discomfort += absolute_difference
        # If the current discomfort is less than the minimum discomfort, update the minimum discomfort and the optimal ordering
        if current_discomfort < min_discomfort:
            min_discomfort = current_discomfort
            optimal_ordering = sorted_heights[(start):] + sorted_heights[:start]
    # Return the optimal ordering
    return optimal_ordering

