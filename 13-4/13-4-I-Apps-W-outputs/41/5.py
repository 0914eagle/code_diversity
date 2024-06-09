
def solve(n, a):
    # Initialize the winner as the first player
    winner = "First"

    # Loop through each pile and remove stones
    for i in range(n):
        # If the current pile has no stones, skip it
        if a[i] == 0:
            continue

        # If the current pile has only one stone, remove it and continue
        if a[i] == 1:
            a[i] -= 1
            continue

        # If the current pile has more than one stone, remove all but one stone
        a[i] -= a[i] - 1

    # If all piles are empty, the second player wins
    if all(a[i] == 0 for i in range(n)):
        winner = "Second"

    return winner

