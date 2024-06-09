
def solve(n, heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the minimum discomfort to a large value
    min_discomfort = float('inf')
    # Initialize the optimal solution
    optimal_solution = []
    # Iterate over all possible starting points
    for i in range(n):
        # Calculate the discomfort of the current solution
        discomfort = 0
        for j in range(n):
            # Calculate the absolute difference between the current and next child's height
            diff = abs(heights[j] - heights[(j+1)%n])
            # Add the absolute difference to the total discomfort
            discomfort += diff
        # If the current solution has a smaller discomfort than the optimal solution, update the optimal solution
        if discomfort < min_discomfort:
            min_discomfort = discomfort
            optimal_solution = heights[:]
    # Return the optimal solution
    return optimal_solution

