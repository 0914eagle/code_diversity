
def solve(n, heights):
    # Sort the heights in non-decreasing order
    sorted_heights = sorted(heights)

    # Initialize the minimum discomfort to a large value
    min_discomfort = float('inf')

    # Initialize the optimal ordering to an empty list
    optimal_ordering = []

    # Iterate over all possible orderings
    for i in range(n):
        # Create a copy of the sorted heights list
        current_ordering = sorted_heights[:]

        # Insert the current height at the correct position in the ordering
        current_ordering.insert(i, heights[i])

        # Calculate the discomfort of the current ordering
        discomfort = calculate_discomfort(current_ordering)

        # If the current ordering has a smaller discomfort than the minimum discomfort, update the minimum discomfort and the optimal ordering
        if discomfort < min_discomfort:
            min_discomfort = discomfort
            optimal_ordering = current_ordering

    # Return the optimal ordering
    return optimal_ordering

def calculate_discomfort(ordering):
    # Initialize the discomfort to zero
    discomfort = 0

    # Iterate over all pairs of adjacent elements in the ordering
    for i in range(len(ordering) - 1):
        # Calculate the absolute difference between the current and next element
        absolute_difference = abs(ordering[i] - ordering[i + 1])

        # Add the absolute difference to the discomfort
        discomfort += absolute_difference

    # Return the discomfort
    return discomfort

n = int(input())
heights = list(map(int, input().split()))
print(solve(n, heights))

