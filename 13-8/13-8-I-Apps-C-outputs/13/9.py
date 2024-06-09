
def solve(n, k, a):
    # Initialize a set to store the divine digits
    divine_digits = set()

    # Iterate over the banknote denominations
    for i in range(n):
        # Get the current banknote value
        value = a[i]

        # Iterate over the possible values of the last digit
        for j in range(k):
            # Calculate the total value of the banknotes
            total_value = value * (k**j)

            # Check if the last digit is divine
            if str(total_value)[-1] == str(j):
                # Add the divine digit to the set
                divine_digits.add(j)

    # Return the number of divine digits and the set of divine digits
    return len(divine_digits), divine_digits

