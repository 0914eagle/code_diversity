
def solve(n, k, a):
    # Initialize a set to store the happy digits
    happy_digits = set()

    # Iterate over the banknote denominations
    for i in range(n):
        # Get the current banknote value
        value = a[i]

        # Iterate over the possible digits
        for digit in range(k):
            # Check if the current digit is the happy digit
            if digit == value % k:
                # Add the happy digit to the set
                happy_digits.add(digit)

    # Return the number of happy digits and the set of happy digits
    return len(happy_digits), happy_digits

