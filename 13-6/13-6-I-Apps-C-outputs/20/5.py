
def get_suitable_values(coins, k):
    # Sort the coins in descending order
    coins.sort(reverse=True)
    # Initialize a variable to store the suitable values
    suitable_values = set()
    # Initialize a variable to keep track of the current sum
    current_sum = 0
    # Iterate through the coins
    for coin in coins:
        # If the current sum is less than the target sum, add the current coin to the current sum
        if current_sum < k:
            current_sum += coin
        # If the current sum is equal to the target sum, add it to the suitable values
        if current_sum == k:
            suitable_values.add(current_sum)
        # If the current sum is greater than the target sum, we can't make the target sum with the remaining coins
        if current_sum > k:
            break
    return suitable_values

