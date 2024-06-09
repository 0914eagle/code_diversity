
def get_min_operations(balances):
    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Loop through the balances and find the bank with the largest balance
    largest_balance = max(balances)
    largest_balance_index = balances.index(largest_balance)

    # Loop through the balances again and find the bank with the smallest balance
    smallest_balance = min(balances)
    smallest_balance_index = balances.index(smallest_balance)

    # Calculate the difference between the largest and smallest balances
    balance_difference = largest_balance - smallest_balance

    # If the difference is positive, transfer the difference from the largest balance to the smallest balance
    if balance_difference > 0:
        min_operations += 1
        balances[largest_balance_index] -= balance_difference
        balances[smallest_balance_index] += balance_difference

    # Return the minimum number of operations required to change the balance of each bank to zero
    return min_operations

if __name__ == '__main__':
    balances = [5, 0, -5]
    print(get_min_operations(balances))

