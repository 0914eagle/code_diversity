
def withdraw_money(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # While the current amount is less than the target amount
    while current_amount < N:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # If so, add the appropriate amount to the current amount
            current_amount += current_amount % 6 == 0 and 6 or 9
        else:
            # If not, add 1 yen to the current amount
            current_amount += 1

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

