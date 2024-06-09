
def solve(N):
    # Initialize variables
    operations = 0
    curr_amount = 0

    # While the current amount is less than the target amount
    while curr_amount < N:
        # If the current amount is less than 9, withdraw 1 yen
        if curr_amount < 9:
            curr_amount += 1
        # If the current amount is between 9 and 81, withdraw 9 yen
        elif curr_amount < 81:
            curr_amount += 9
        # If the current amount is between 81 and 216, withdraw 36 yen
        elif curr_amount < 216:
            curr_amount += 36
        # If the current amount is between 216 and 729, withdraw 81 yen
        elif curr_amount < 729:
            curr_amount += 81
        # If the current amount is greater than or equal to 729, withdraw 216 yen
        else:
            curr_amount += 216

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

