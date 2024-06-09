
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}

    # Iterate over the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])

        # Iterate over the possible next cards
        for next_card in dp:
            # Get the current card and the next card
            current_card, next_card = card, (next_card[0], next_card[1] + 1)

            # If the next card is within the given range
            if next_card[1] <= m:
                # Increment the number of ways to get the next card
                dp[next_card] = dp.get(next_card, 0) + dp[current_card]

            # If the current card is even
            if current_card[0] % 2 == 0:
                # Get the half of the current card
                half_card = (current_card[0] // 2, current_card[1] // 2)

                # If the half card is within the given range
                if half_card[1] <= m:
                    # Increment the number of ways to get the half card
                    dp[half_card] = dp.get(half_card, 0) + dp[current_card]

    # Return the number of ways to get the required cards
    return sum(dp.values())

