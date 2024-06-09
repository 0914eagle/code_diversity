
def solve(n, B, arr):
    # Sort the array in non-decreasing order
    arr.sort()

    # Initialize variables to keep track of the number of cuts and the current cost
    cuts = 0
    cost = 0

    # Loop through the array and check if the current element is a cut
    for i in range(n - 1):
        # Calculate the cost of the current cut
        cut_cost = abs(arr[i] - arr[i + 1])

        # Check if the current cut is within budget
        if cost + cut_cost <= B:
            # Increment the number of cuts and add the cost of the current cut to the total cost
            cuts += 1
            cost += cut_cost

    # Return the maximum number of cuts possible within budget
    return cuts

