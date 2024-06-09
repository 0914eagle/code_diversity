
def solve(n):
    # Initialize the minimum difference to a large value
    min_diff = 1000000000
    # Loop through all possible values of the sum of set A
    for a in range(1, n + 1):
        # Calculate the sum of set B as the total sum minus the sum of set A
        b = n - a
        # Calculate the absolute difference between the sums of set A and set B
        diff = abs(a - b)
        # If the difference is smaller than the minimum difference, update the minimum difference
        if diff < min_diff:
            min_diff = diff
    # Return the minimum difference
    return min_diff

