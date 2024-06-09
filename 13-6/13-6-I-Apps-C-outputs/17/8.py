
def solve(n, crush):
    # Initialize a list to store the number of rounds required for each person to become the Joon-Joon
    rounds = [0] * (n + 1)
    # Loop through each person and calculate the number of rounds required for them to become the Joon-Joon
    for i in range(1, n + 1):
        # If the person is their own crush, they can become the Joon-Joon in one round
        if i == crush[i - 1]:
            rounds[i] = 1
        # Otherwise, they need to call their crush and their crush's crush, and so on, until they reach their own crush
        else:
            rounds[i] = 1 + rounds[crush[i - 1]]
    # Find the minimum number of rounds required for any person to become the Joon-Joon
    min_rounds = min(rounds)
    # If no person can become the Joon-Joon, return -1
    if min_rounds == 0:
        return -1
    # Otherwise, return the minimum number of rounds required for any person to become the Joon-Joon
    else:
        return min_rounds

