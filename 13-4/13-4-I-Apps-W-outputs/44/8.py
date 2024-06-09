
def solve(sequence, k):
    n = len(sequence)
    if n == 1:
        return 0
    if k == 0:
        return abs(sequence[0] - sequence[-1])
    # Sort the sequence in non-decreasing order
    sequence.sort()
    # Initialize the minimum difference and the current difference
    min_diff = abs(sequence[0] - sequence[-1])
    curr_diff = min_diff
    # Loop through each element in the sequence
    for i in range(n):
        # If the current difference is less than the minimum difference, update the minimum difference
        if curr_diff < min_diff:
            min_diff = curr_diff
        # If the current element is not the maximum or minimum element, try increasing and decreasing it
        if i > 0 and i < n-1:
            # Increase the current element by 1 and calculate the difference
            sequence[i] += 1
            curr_diff = abs(sequence[0] - sequence[-1])
            # If the difference is less than the minimum difference, update the minimum difference
            if curr_diff < min_diff:
                min_diff = curr_diff
            # Decrease the current element by 1 and calculate the difference
            sequence[i] -= 2
            curr_diff = abs(sequence[0] - sequence[-1])
            # If the difference is less than the minimum difference, update the minimum difference
            if curr_diff < min_diff:
                min_diff = curr_diff
        # If the current element is the maximum element, try decreasing it
        if i == n-1:
            # Decrease the current element by 1 and calculate the difference
            sequence[i] -= 1
            curr_diff = abs(sequence[0] - sequence[-1])
            # If the difference is less than the minimum difference, update the minimum difference
            if curr_diff < min_diff:
                min_diff = curr_diff
    # Return the minimum difference
    return min_diff

