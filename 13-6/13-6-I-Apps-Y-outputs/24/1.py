
def solve(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # While the current amount is less than the target amount
    while current_amount < N:
        # If the current amount is less than 6, withdraw 1 yen
        if current_amount < 6:
            current_amount += 1
        # If the current amount is greater than or equal to 6 but less than 36, withdraw 6 yen
        elif current_amount >= 6 and current_amount < 36:
            current_amount += 6
        # If the current amount is greater than or equal to 36 but less than 81, withdraw 9 yen
        elif current_amount >= 36 and current_amount < 81:
            current_amount += 9
        # If the current amount is greater than or equal to 81, withdraw 1 yen
        else:
            current_amount += 1

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

