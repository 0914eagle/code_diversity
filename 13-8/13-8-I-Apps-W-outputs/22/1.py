
def solve(n, c, t):
    # Check if the number of stones is valid
    if n < 2 or n > 10**5:
        return "No"

    # Check if the charges of the stones are valid
    for i in range(n):
        if c[i] < 0 or c[i] > 2 * 10**9:
            return "No"

    # Check if the charges of Andrew's stones are valid
    for i in range(n):
        if t[i] < 0 or t[i] > 2 * 10**9:
            return "No"

    # Initialize the charges of Grigory's stones as a list of tuples (charge, index)
    charges = [(c[i], i) for i in range(n)]

    # Sort the charges in descending order
    charges.sort(reverse=True)

    # Initialize the charges of Andrew's stones as a list of tuples (charge, index)
    targets = [(t[i], i) for i in range(n)]

    # Sort the charges in descending order
    targets.sort(reverse=True)

    # Loop through the charges of Grigory's stones and try to find a matching charge in Andrew's stones
    for i in range(n):
        # Check if the current charge is equal to the target charge
        if charges[i][0] == targets[i][0]:
            # If it is, remove both charges from the list
            charges.pop(i)
            targets.pop(i)
        # If it is not, break the loop
        else:
            break

    # Check if all the charges have been removed
    if not charges and not targets:
        return "Yes"
    else:
        return "No"

