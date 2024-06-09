
def max_cuts(n, B, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum number of cuts to 0
    max_cuts = 0
    # Initialize the current cost to 0
    cost = 0
    # Iterate through the array
    for i in range(n - 1):
        # Calculate the cost of the current cut
        cost += arr[i + 1] - arr[i]
        # Check if the current cost is less than or equal to the budget
        if cost <= B:
            # Increment the maximum number of cuts
            max_cuts += 1
        else:
            # Break the loop
            break
    # Return the maximum number of cuts
    return max_cuts

