
def solve(n, a):
    # Initialize the winner as the first player
    winner = "First"

    # Loop through each pile and remove stones
    for i in range(n):
        # If the current pile has at least one stone, remove one stone
        if a[i] > 0:
            a[i] -= 1
        # If the current pile is empty, switch the winner
        elif a[i] == 0:
            winner = "Second"

    # Return the winner
    return winner

