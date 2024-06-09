
def get_min_operations(balances):
    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Loop through the balances and find the bank with the largest absolute balance
    largest_balance = 0
    for i, balance in enumerate(balances):
        if abs(balance) > largest_balance:
            largest_balance = abs(balance)
            largest_balance_index = i

    # Loop through the balances and find the bank with the second largest absolute balance
    second_largest_balance = 0
    for i, balance in enumerate(balances):
        if i != largest_balance_index and abs(balance) > second_largest_balance:
            second_largest_balance = abs(balance)
            second_largest_balance_index = i

    # Calculate the minimum number of operations required to transfer the largest balance to the second largest balance
    min_operations += abs(largest_balance - second_largest_balance)

    # Update the balances to reflect the transfer
    balances[largest_balance_index] = 0
    balances[second_largest_balance_index] += largest_balance - second_largest_balance

    # Loop through the balances and find the bank with the largest absolute balance after the first transfer
    largest_balance = 0
    for i, balance in enumerate(balances):
        if abs(balance) > largest_balance and i != largest_balance_index and i != second_largest_balance_index:
            largest_balance = abs(balance)
            largest_balance_index = i

    # Calculate the minimum number of operations required to transfer the largest balance to the second largest balance
    min_operations += abs(largest_balance - second_largest_balance)

    # Update the balances to reflect the transfer
    balances[largest_balance_index] = 0
    balances[second_largest_balance_index] += largest_balance - second_largest_balance

    # Return the minimum number of operations required to change the balance of each bank to zero
    return min_operations

