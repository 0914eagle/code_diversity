
def solve(n, c, t):
    # Check if the number of stones is valid
    if n < 2 or n > 10**5:
        return "No"

    # Check if the charges are valid
    for i in range(n):
        if c[i] < 0 or c[i] > 2 * 10**9:
            return "No"

    # Check if the charges of Grigory's stones can be transformed into the charges of Andrew's stones
    for i in range(n):
        if c[i] != t[i]:
            return "No"

    # If all the charges are equal, return "Yes"
    return "Yes"

