
def get_max_coins(d, g, n, k):
    # Initialize variables
    max_coins = 0
    distracted_rounds = 0

    # Loop through each round
    for i in range(n):
        # If Gladstone is distracted, Donald can look at his cards and swap them
        if distracted_rounds < k:
            distracted_rounds += 1
        # Otherwise, Donald needs to choose his bet carefully
        else:
            # If Donald has more coins than Gladstone, he can bet all his coins
            if d > g:
                d = 0
                g = 0
            # Otherwise, Donald needs to bet some of his coins
            else:
                d = 0
                g -= d

        # Update the maximum number of coins
        max_coins = max(max_coins, d + g)

    return max_coins

