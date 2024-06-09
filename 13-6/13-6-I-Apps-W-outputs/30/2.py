
def solve(heights):
    n = len(heights)
    # Sort the heights in non-decreasing order
    sorted_heights = sorted(heights)
    # Initialize the minimum discomfort to a large value
    min_discomfort = float('inf')
    # Initialize the optimal order to an empty list
    optimal_order = []
    # Iterate over all possible starting points
    for i in range(n):
        # Calculate the discomfort of the current circle
        discomfort = 0
        for j in range(n):
            # Calculate the absolute difference between the current and next height
            abs_diff = abs(sorted_heights[j] - sorted_heights[(j+i)%n])
            # Add the absolute difference to the total discomfort
            discomfort += abs_diff
        # If the current circle has a smaller discomfort than the minimum discomfort, update the minimum discomfort and the optimal order
        if discomfort < min_discomfort:
            min_discomfort = discomfort
            optimal_order = sorted_heights[(i+1)%n:n+i] + sorted_heights[0:i]
    # Return the optimal order
    return optimal_order

