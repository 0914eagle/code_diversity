
def solve(n, k, a):
    # Initialize a set to store the divine digits
    divine_digits = set()

    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]

        # Iterate over the possible values of the last digit
        for d in range(k):
            # Check if the current value plus the last digit is a multiple of the current banknote
            if (value + d) % a[i] == 0:
                # Add the last digit to the set of divine digits
                divine_digits.add(d)

    # Return the number of divine digits and the set of divine digits
    return len(divine_digits), divine_digits

