
def get_min_operations(balances):
    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Loop through the balances and find the bank with the largest absolute balance
    largest_balance = max(balances, key=abs)

    # While the largest balance is not 0, perform operations
    while largest_balance != 0:
        # Find the bank with the next largest absolute balance
        next_largest_balance = max(balances, key=abs)

        # If the next largest balance is 0, break out of the loop
        if next_largest_balance == 0:
            break

        # Perform an operation to transfer the difference between the largest and next largest balance
        # to the next largest balance
        balances[balances.index(largest_balance)] += balances[balances.index(next_largest_balance)]
        balances[balances.index(next_largest_balance)] = 0

        # Increment the minimum number of operations
        min_operations += 1

        # Update the largest balance to the next largest balance
        largest_balance = next_largest_balance

    # Return the minimum number of operations
    return min_operations

