
def get_max_cuts(n, B, a):
    # Sort the array in non-decreasing order
    a.sort()

    # Initialize variables to keep track of the current cost and number of cuts
    cost = 0
    num_cuts = 0

    # Loop through the array and check if the current element is a cut point
    for i in range(n - 1):
        # Check if the current element is a cut point
        if a[i] % 2 != a[i + 1] % 2:
            # Calculate the cost of the current cut
            cost += abs(a[i] - a[i + 1])

            # Check if the current cost exceeds the budget
            if cost > B:
                # If it does, return the current number of cuts
                return num_cuts

            # Increment the number of cuts
            num_cuts += 1

    # If we reach the end of the array and the cost is still within budget, return the number of cuts
    return num_cuts

