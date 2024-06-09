
def solve(n, k, a):
    # Convert the denominations to a list of digits
    digits = [int(digit) for digit in str(a)]

    # Initialize a set to store the happy digits
    happy_digits = set()

    # Iterate over the digits
    for digit in digits:
        # Check if the digit is happy
        if digit % k == 0:
            happy_digits.add(digit)

    # Return the happy digits
    return len(happy_digits), sorted(list(happy_digits))

