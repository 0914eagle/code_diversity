
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}

    # Iterate through the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])

        # Iterate through the previous cards
        for prev_card in dp:
            # Get the previous card's values
            prev_a, prev_b = prev_card

            # If the previous card's values are even, multiply them by 2 to get the new card's values
            if prev_a % 2 == 0 and prev_b % 2 == 0:
                new_a = prev_a // 2
                new_b = prev_b // 2
                new_card = (new_a, new_b)

                # If the new card is not already in the dictionary, add it and set the number of ways to get it to the number of ways to get the previous card
                if new_card not in dp:
                    dp[new_card] = dp[prev_card]

            # If the previous card's values are not even, add 1 to the first value and 1 to the second value to get the new card's values
            else:
                new_a = prev_a + 1
                new_b = prev_b + 1
                new_card = (new_a, new_b)

                # If the new card is not already in the dictionary, add it and set the number of ways to get it to the number of ways to get the previous card
                if new_card not in dp:
                    dp[new_card] = dp[prev_card]

    # Return the number of ways to get the required cards
    return dp[(1, m)]

