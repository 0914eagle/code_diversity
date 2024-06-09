
def solve(n, crush):
    # Initialize a list to store the number of rounds required for each person to become the Joon-Joon
    rounds = [0] * (n + 1)
    # Loop through each person and their crush
    for i in range(1, n + 1):
        # If the person is their own crush, they become the Joon-Joon in 1 round
        if i == crush[i - 1]:
            rounds[i] = 1
        # Otherwise, find the number of rounds required for the person's crush to become the Joon-Joon
        else:
            rounds[i] = rounds[crush[i - 1]] + 1
    # Find the smallest number of rounds required for any person to become the Joon-Joon
    min_rounds = min(rounds)
    # If there is no smallest number of rounds, return -1
    if min_rounds == 0:
        return -1
    # Otherwise, return the smallest number of rounds
    return min_rounds

