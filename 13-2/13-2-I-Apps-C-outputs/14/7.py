
def solve(n, k, a):
    # Initialize a set to store the divine digits
    divine_digits = set()

    # Iterate over the denominations of banknotes
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]

        # Iterate over the digits of the value
        for digit in str(value):
            # Check if the digit is the divine digit
            if digit == str(k - 1):
                # Add the divine digit to the set
                divine_digits.add(digit)

    # Return the number of divine digits and the set of divine digits
    return len(divine_digits), divine_digits

