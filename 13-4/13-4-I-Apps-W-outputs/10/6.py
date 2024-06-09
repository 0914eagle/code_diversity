
def solve(n, B, arr):
    # Sort the array in non-decreasing order
    arr.sort()

    # Initialize variables to keep track of the number of cuts and the current cost
    cuts = 0
    cost = 0

    # Loop through the array and check if the current element is a cut
    for i in range(n - 1):
        # Check if the current element is a cut
        if arr[i] % 2 != arr[i + 1] % 2:
            # Calculate the cost of the cut
            cost += abs(arr[i] - arr[i + 1])

            # Check if the cost exceeds the budget
            if cost > B:
                # If the cost exceeds the budget, return the current number of cuts
                return cuts

            # Increment the number of cuts
            cuts += 1

    # If the cost does not exceed the budget, return the total number of cuts
    return cuts

