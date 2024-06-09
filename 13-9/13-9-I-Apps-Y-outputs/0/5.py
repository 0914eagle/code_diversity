
def solve(N):
    # Initialize variables
    operations = 0
    curr_amount = 0

    # While the current amount is less than the target amount
    while curr_amount < N:
        # If the current amount is divisible by 6, withdraw 6 yen
        if curr_amount % 6 == 0:
            curr_amount += 6
        # If the current amount is divisible by 9, withdraw 9 yen
        elif curr_amount % 9 == 0:
            curr_amount += 9
        # If the current amount is not divisible by 6 or 9, withdraw 1 yen
        else:
            curr_amount += 1

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

