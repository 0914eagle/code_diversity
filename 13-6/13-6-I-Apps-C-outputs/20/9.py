
def get_suitable_values(coins, k):
    # Sort the coins in ascending order
    coins.sort()
    # Initialize a list to store the suitable values
    suitable_values = []
    # Iterate over the coins
    for i in range(len(coins)):
        # Check if the sum of the current coin and all the previous coins is equal to the price
        if sum(coins[:i+1]) == k:
            # Add the current coin to the list of suitable values
            suitable_values.append(coins[i])
    return suitable_values

