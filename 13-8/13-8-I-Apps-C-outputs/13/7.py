
def solve(n, k, a):
    # Calculate the maximum amount that can be made with the given banknotes
    max_amount = sum(a)

    # Initialize a list to store the divine digits
    divine_digits = []

    # Iterate from 0 to k - 1
    for i in range(k):
        # Check if the last digit of the maximum amount is equal to i
        if str(max_amount)[-1] == str(i):
            # If it is, add it to the list of divine digits
            divine_digits.append(i)

    # Return the number of divine digits and the list of divine digits
    return len(divine_digits), divine_digits

