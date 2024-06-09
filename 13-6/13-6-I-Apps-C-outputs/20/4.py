
def get_suitable_values(coins, k):
    # Calculate the sum of all coins
    total = sum(coins)
    
    # Initialize a set to store the suitable values
    suitable_values = set()
    
    # Loop through all possible combinations of coins
    for i in range(1, total + 1):
        # Check if the current combination sums up to k
        if i == k:
            # Add the current combination to the suitable values
            suitable_values.add(i)
        # Check if the current combination is a subset of k
        elif i < k and k % i == 0:
            # Add the current combination to the suitable values
            suitable_values.add(i)
    
    return suitable_values

