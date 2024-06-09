
def solve(m, n, p, q):
    # Initialize a list to store the digits of the number
    digits = []
    # Loop through the range of numbers from 1 to 9
    for i in range(1, 10):
        # Check if the current number is a valid starting digit
        if i != 0:
            # Add the current number to the list of digits
            digits.append(i)
            # Recursively call the function to find the remaining digits
            recurse(m, n, p, q, digits)
            # If the function returns a valid number, return it
            if len(digits) == m:
                return "".join(map(str, digits))
            # If the function returns None, remove the current digit and try again
            else:
                digits.pop()
    # If no valid number is found, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

def recurse(m, n, p, q, digits):
    # If we have found all the digits, return the list of digits
    if len(digits) == m:
        return digits
    # If we have reached the maximum number of digits, return None
    if len(digits) == 10:
        return None
    # Add the current number to the list of digits
    digits.append(digits[-1] + 1)
    # Recursively call the function to find the remaining digits
    recurse(m, n, p, q, digits)
    # If the function returns a valid number, return it
    if len(digits) == m:
        return digits
    # If the function returns None, remove the current digit and try again
    else:
        digits.pop()
        return recurse(m, n, p, q, digits)

