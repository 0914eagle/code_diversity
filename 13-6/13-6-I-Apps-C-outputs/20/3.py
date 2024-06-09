
def get_suitable_values(coins, k):
    # Calculate the sum of all coins
    total = sum(coins)
    
    # Initialize a set to store the suitable values
    suitable_values = set()
    
    # Iterate through all possible subsets of coins
    for i in range(1, len(coins) + 1):
        # Get the sum of the current subset of coins
        current_sum = sum(coins[:i])
        
        # Check if the current sum is equal to the price of the chocolate
        if current_sum == k:
            # Add the current sum to the suitable values set
            suitable_values.add(current_sum)
        # Check if the current sum is less than the price of the chocolate
        elif current_sum < k:
            # Recursively call the function with the remaining coins and the remaining price
            suitable_values |= get_suitable_values(coins[i:], k - current_sum)
    
    return suitable_values

