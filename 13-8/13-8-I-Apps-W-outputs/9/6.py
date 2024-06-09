
def solve(n, B, arr):
    # Sort the array in non-decreasing order
    arr.sort()

    # Initialize variables to keep track of the number of cuts and the current budget
    cuts = 0
    budget = B

    # Iterate through the array and check if the current element is within budget
    for i in range(n - 1):
        # Calculate the cost of the current cut
        cost = abs(arr[i] - arr[i + 1])

        # Check if the current cut is within budget
        if cost <= budget:
            # Increment the number of cuts and decrement the budget
            cuts += 1
            budget -= cost

    # Return the maximum number of cuts possible with the given budget
    return cuts

