
def get_min_operations(balances):
    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Loop through the balances and find the bank with the largest balance
    largest_balance = max(balances)

    # Loop through the balances again and find the bank with the smallest balance
    smallest_balance = min(balances)

    # Calculate the difference between the largest and smallest balance
    balance_diff = largest_balance - smallest_balance

    # If the difference is positive, we need to transfer money from the bank with the largest balance to the bank with the smallest balance
    if balance_diff > 0:
        # Calculate the minimum number of operations required to transfer the difference
        min_operations += balance_diff

        # Update the balances to reflect the transfer
        balances[largest_balance] -= balance_diff
        balances[smallest_balance] += balance_diff

    # If the difference is negative, we need to transfer money from the bank with the smallest balance to the bank with the largest balance
    elif balance_diff < 0:
        # Calculate the minimum number of operations required to transfer the difference
        min_operations += abs(balance_diff)

        # Update the balances to reflect the transfer
        balances[largest_balance] += abs(balance_diff)
        balances[smallest_balance] -= abs(balance_diff)

    # Return the minimum number of operations required to make all balances equal
    return min_operations

