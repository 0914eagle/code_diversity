
def get_max_coins(d, g, n, k):
    # Initialize the maximum coins that Donald can have
    max_coins = 0
    
    # Loop through each round
    for round in range(1, n + 1):
        # If Gladstone is distracted, Donald can look at his cards and swap them to ensure a win
        if round <= k:
            # If Donald has more coins than Gladstone, Donald can win the round
            if d > g:
                # Update the maximum coins that Donald can have
                max_coins = max(max_coins, d + g)
            # If Gladstone has more coins than Donald, Donald can still win the round by swapping his cards
            else:
                # Update the maximum coins that Donald can have
                max_coins = max(max_coins, g)
        # If Gladstone is not distracted, Donald has no advantage and his coins will be lost
        else:
            # Update the maximum coins that Donald can have
            max_coins = max(max_coins, 0)
    
    # Return the maximum coins that Donald can have
    return max_coins

