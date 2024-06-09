
def solve(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # While the current amount is less than the target amount
    while current_amount < N:
        # If the current amount is less than 9, withdraw 1 yen
        if current_amount < 9:
            current_amount += 1
        # If the current amount is greater than or equal to 9, withdraw 9 yen
        else:
            current_amount += 9
        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

