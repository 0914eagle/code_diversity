
def solve(sequence, k):
    n = len(sequence)
    if n == 1:
        return 0
    if k == 0:
        return max(sequence) - min(sequence)
    # Sort the sequence in non-decreasing order
    sequence.sort()
    # Initialize the minimum difference and the current difference
    min_diff = float('inf')
    curr_diff = sequence[n-1] - sequence[0]
    # Loop through each element and check if increasing or decreasing it by 1 helps
    for i in range(n):
        # Increase the element by 1
        sequence[i] += 1
        # Calculate the current difference
        curr_diff = max(sequence) - min(sequence)
        # If the current difference is less than the minimum difference, update the minimum difference
        if curr_diff < min_diff:
            min_diff = curr_diff
        # Decrease the element by 1
        sequence[i] -= 1
    # Return the minimum difference
    return min_diff

