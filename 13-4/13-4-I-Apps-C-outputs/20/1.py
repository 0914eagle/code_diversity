
def solve(m, n, p, q):
    # Initialize a list to store the digits of the number
    digits = []
    # Loop through the range of numbers from 1 to 9
    for i in range(1, 10):
        # Check if the current number is a valid starting digit
        if i != 0:
            # Add the current digit to the list of digits
            digits.append(i)
            # Recursively call the function to find the remaining digits
            recurse(m, n, p, q, digits)
            # Remove the current digit from the list of digits
            digits.pop()

def recurse(m, n, p, q, digits):
    # Check if we have found the required number of digits
    if len(digits) == m:
        # Check if the number is valid
        if is_valid(digits, n, p, q):
            # Print the number
            print(int("".join(map(str, digits))))
            return
    # Loop through the range of numbers from 0 to 9
    for i in range(0, 10):
        # Check if the current number is a valid digit
        if i != 0:
            # Add the current digit to the list of digits
            digits.append(i)
            # Recursively call the function to find the remaining digits
            recurse(m, n, p, q, digits)
            # Remove the current digit from the list of digits
            digits.pop()

def is_valid(digits, n, p, q):
    # Initialize a variable to store the result
    result = True
    # Loop through the range of numbers from 0 to n-1
    for i in range(0, n):
        # Check if the current digit is not equal to the first digit of p
        if digits[i] != p[0]:
            # Set the result to False
            result = False
            break
    # Loop through the range of numbers from n to m-1
    for i in range(n, len(digits)):
        # Check if the current digit is not equal to the corresponding digit of p
        if digits[i] != p[i-n]:
            # Set the result to False
            result = False
            break
    # Return the result
    return result

m, n, p, q = map(int, input().split())
solve(m, n, p, q)

