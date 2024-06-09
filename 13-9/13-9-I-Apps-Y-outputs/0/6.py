
def solve(n):
    # Initialize variables
    operations = 0
    current = 0

    # While the total amount withdrawn is less than the given amount
    while current < n:
        # If the current amount is divisible by 6, withdraw 6 yen
        if current % 6 == 0:
            current += 6
        # If the current amount is divisible by 9, withdraw 9 yen
        elif current % 9 == 0:
            current += 9
        # Otherwise, withdraw 1 yen
        else:
            current += 1

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

