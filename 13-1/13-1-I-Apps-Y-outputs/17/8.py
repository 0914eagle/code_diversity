
def f1(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # Loop until we reach the desired amount
    while current_amount < N:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # If it is, add the corresponding amount
            current_amount += current_amount
            operations += 1
        else:
            # If it's not, add 1 yen
            current_amount += 1
            operations += 1

    # Return the number of operations required
    return operations

