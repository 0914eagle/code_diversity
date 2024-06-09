
def solve(n, k, a):
    # Convert the input denomination to a list
    a = list(a)

    # Initialize the count of happy digits
    count = 0

    # Initialize the list of happy digits
    happy_digits = []

    # Loop through each denomination
    for i in range(n):
        # Get the value of the current denomination
        value = a[i]

        # Loop through each digit in the value
        for digit in str(value):
            # Check if the digit is a happy digit
            if digit in str(k):
                # Increment the count of happy digits
                count += 1

                # Add the digit to the list of happy digits
                happy_digits.append(digit)

    # Return the count of happy digits and the list of happy digits
    return count, happy_digits

