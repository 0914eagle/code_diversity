
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}

    # Iterate over the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])

        # Iterate over the possible previous cards
        for prev_card in dp:
            # Get the number of ways to get the current card from the previous card
            num_ways = dp[prev_card]

            # If the previous card is gray, we can get a new card by painting a new (a + 1, b + 1) card
            if prev_card[0] == 1:
                new_card = (prev_card[1] + 1, prev_card[1] + 1)
                dp[new_card] = dp.get(new_card, 0) + num_ways

            # If the previous card is white, we can get a new card by painting a new (a / 2, b / 2) card
            if prev_card[0] == 2:
                new_card = (prev_card[1] // 2, prev_card[1] // 2)
                dp[new_card] = dp.get(new_card, 0) + num_ways

            # If the previous card is gray-and-white, we can get a new card by painting a new (a, c) card
            if prev_card[0] == 3:
                new_card = (prev_card[1], prev_card[2])
                dp[new_card] = dp.get(new_card, 0) + num_ways

    # Return the number of ways to get the required cards
    return sum(dp.values())

