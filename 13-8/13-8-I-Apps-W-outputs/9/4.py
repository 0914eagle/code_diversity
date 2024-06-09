
def solve(n, B, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize variables to keep track of the number of cuts and the current cost
    cuts, cost = 0, 0
    # Loop through the array and check if the current element is within the budget
    for i in range(n - 1):
        # Calculate the cost of the current cut
        cost += abs(a[i] - a[i + 1])
        # Check if the current cost is less than or equal to the budget
        if cost <= B:
            # Increment the number of cuts
            cuts += 1
        else:
            # If the current cost is greater than the budget, break the loop
            break
    # Return the number of cuts
    return cuts

