
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}

    # Iterate over the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])

        # Iterate over the previous cards
        for prev_card in dp:
            # Get the number of ways to get the current card from the previous card
            num_ways = dp[prev_card]

            # If the previous card is gray, we can get a new card with (a + 1, b + 1)
            if prev_card[0] == 1:
                new_card = (card[0] + 1, card[1] + 1)
                dp[new_card] = dp.get(new_card, 0) + num_ways

            # If the previous card is white, we can get a new card with (a / 2, b / 2)
            if prev_card[1] % 2 == 0:
                new_card = (prev_card[0] // 2, prev_card[1] // 2)
                dp[new_card] = dp.get(new_card, 0) + num_ways

            # If the previous card is gray-and-white, we can get a new card with (a, c)
            if prev_card[0] == 1 and prev_card[1] % 2 == 0:
                new_card = (prev_card[0], card[1])
                dp[new_card] = dp.get(new_card, 0) + num_ways

    # Return the number of ways to get all the required cards
    return sum(dp.values())

