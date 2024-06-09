
def solve(n, a):
    # Initialize the winner as the first player
    winner = "First"

    # Loop through each pile and remove stones
    for i in range(n):
        # If the current pile is empty, switch the winner
        if a[i] == 0:
            winner = "Second"
        # Remove the minimum number of stones from the current pile
        else:
            a[i] -= 1

    # Return the winner
    return winner

