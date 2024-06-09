
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
    # If no valid number was found, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

def recurse(m, n, p, q, digits):
    # If we have found all the digits, multiply the number by q and return it
    if len(digits) == m:
        result = int("".join(map(str, digits))) * q
        return str(result)
    # Loop through the range of numbers from 0 to 9
    for i in range(0, 10):
        # Check if the current number is a valid digit
        if i != 0:
            # Add the current number to the list of digits
            digits.append(i)
            # Recursively call the function to find the remaining digits
            recurse(m, n, p, q, digits)
            # Remove the current number from the list of digits
            digits.pop()

