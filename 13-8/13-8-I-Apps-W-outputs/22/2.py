
def solve(n, c, t):
    # Check if the number of stones is valid
    if n < 2 or n > 100000:
        return "No"

    # Check if the charges are valid
    for i in range(n):
        if c[i] < 0 or c[i] > 2000000000:
            return "No"

    # Check if the charges of Grigory's stones can be transformed into the charges of Andrew's stones
    for i in range(n):
        if c[i] != t[i]:
            return "No"

    # If all the charges are the same, return "Yes"
    return "Yes"

