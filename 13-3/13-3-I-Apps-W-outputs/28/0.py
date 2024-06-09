
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}

    # Iterate over the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])

        # Iterate over the possible next cards
        for next_card in dp:
            # Get the current card's values
            x, y = card
            # Get the next card's values
            x2, y2 = next_card

            # If the next card's values are valid
            if x2 <= x and y2 >= y:
                # Update the number of ways to get the current card
                dp[card] += dp[next_card]

    # Return the number of ways to get the required cards
    return dp[(1, m)]

