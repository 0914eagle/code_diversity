
def solve(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # While the current amount is less than the target amount
    while current_amount < N:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # If it is, add the corresponding power of 6 or 9
            current_amount += current_amount % 6 ** operations if current_amount % 6 == 0 else current_amount % 9 ** operations
        else:
            # If it is not, add 1 yen
            current_amount += 1

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

