
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
            recursive_solve(m, n, p, q, digits)
            # If a valid number is found, return it
            if len(digits) == m:
                return "".join(map(str, digits))
    # If no valid number is found, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

def recursive_solve(m, n, p, q, digits):
    # If the number of digits is equal to the number of digits to cross out, return
    if len(digits) == n:
        return
    # Loop through the range of numbers from 0 to 9
    for i in range(0, 10):
        # Check if the current number is a valid digit
        if i != 0:
            # Add the current number to the list of digits
            digits.append(i)
            # Recursively call the function to find the remaining digits
            recursive_solve(m, n, p, q, digits)
            # If a valid number is found, return it
            if len(digits) == m:
                return "".join(map(str, digits))
    # If no valid number is found, return
    return

