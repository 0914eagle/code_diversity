
def get_min_operations(balances):
    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Loop through the balances and find the bank with the largest absolute balance
    largest_balance = max(balances, key=abs)

    # While the largest balance is not 0, perform operations
    while largest_balance != 0:
        # Find the bank with the largest absolute balance that is not the current bank
        next_bank = balances.index(largest_balance)

        # Transfer the largest balance to the next bank
        balances[next_bank] += largest_balance
        balances[largest_balance] -= largest_balance

        # Update the largest balance
        largest_balance = max(balances, key=abs)

        # Increment the minimum number of operations
        min_operations += 1

    # Return the minimum number of operations
    return min_operations

