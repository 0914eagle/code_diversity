
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}

    # Iterate over the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])

        # Iterate over the previous cards
        for j in range(i):
            # Get the previous card
            prev_card = (1, a[j])

            # If the previous card is not already in the dictionary, skip it
            if prev_card not in dp:
                continue

            # If the previous card is (1, 1), there is only one way to get it
            if prev_card == (1, 1):
                dp[card] = 1
                continue

            # If the previous card is (x, y) and x is even, there are two ways to get the current card
            if prev_card[0] % 2 == 0:
                dp[card] = dp.get(card, 0) + 2
                continue

            # If the previous card is (x, y) and x is odd, there is one way to get the current card
            dp[card] = dp.get(card, 0) + 1

    # Return the number of ways to get all the required cards
    return sum(dp.values())

