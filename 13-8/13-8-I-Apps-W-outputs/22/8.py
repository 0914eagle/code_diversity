
def solve(n, c, t):
    # Check if the number of stones is valid
    if n < 2 or n > 10**5:
        return "No"

    # Check if the charges of Grigory's stones are valid
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

    # Initialize the result as "Yes"
    result = "Yes"

    # Loop through the charges and check if they can be transformed into Andrew's stones
    for charge, index in charges:
        # Check if the charge is not equal to the corresponding Andrew's stone
        if charge != t[index]:
            # Check if the charge is not equal to the sum of the adjacent charges
            if charge != t[index - 1] + t[index + 1]:
                # If the charge cannot be transformed, return "No"
                result = "No"
                break

    # Return the result
    return result

