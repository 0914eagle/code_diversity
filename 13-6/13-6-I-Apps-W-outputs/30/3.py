
def solve(n, heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the minimum discomfort to a large value
    min_discomfort = float('inf')
    # Initialize the optimal order to an empty list
    optimal_order = []
    # Iterate over all possible orders
    for i in range(n):
        # Calculate the discomfort of the current order
        discomfort = 0
        for j in range(n):
            # Calculate the absolute difference between the current and next child
            abs_diff = abs(heights[j] - heights[(j+1)%n])
            # Add the absolute difference to the total discomfort
            discomfort += abs_diff
        # If the current order has a smaller discomfort than the minimum discomfort, update the minimum discomfort and the optimal order
        if discomfort < min_discomfort:
            min_discomfort = discomfort
            optimal_order = heights[:]
    # Return the optimal order
    return optimal_order

