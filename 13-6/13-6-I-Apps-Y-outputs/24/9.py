
def solve(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # Loop until we reach the target amount or exceed it
    while current_amount < N:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # If it is, add the appropriate amount to the current amount
            current_amount += current_amount % 6 == 0 and 6 or 9
            operations += 1

    # Return the number of operations required
    return operations

