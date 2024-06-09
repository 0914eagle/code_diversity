
def withdraw(N):
    # Initialize variables
    operations = 0
    current = 0

    # Loop until we reach the total amount
    while current < N:
        # Check if the current amount is a power of 6
        if current % 6 == 0:
            # If it is, withdraw 6^x yen
            current += 6 ** (current // 6)
        # Check if the current amount is a power of 9
        elif current % 9 == 0:
            # If it is, withdraw 9^x yen
            current += 9 ** (current // 9)
        # Otherwise, withdraw 1 yen
        else:
            current += 1

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

