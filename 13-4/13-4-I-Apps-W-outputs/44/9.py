
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum difference and the current difference
    min_diff = arr[-1] - arr[0]
    curr_diff = min_diff
    # Loop through each element in the array
    for i in range(n):
        # If the current difference is less than the minimum difference, update the minimum difference
        if curr_diff < min_diff:
            min_diff = curr_diff
        # If the current difference is greater than the minimum difference, break the loop
        if curr_diff > min_diff:
            break
        # Update the current difference by increasing or decreasing the current element by 1
        curr_diff += 2 if arr[i] % 2 == 0 else -2
        # If the current difference is greater than the maximum number of operations, break the loop
        if abs(curr_diff) > k:
            break
    return min_diff

