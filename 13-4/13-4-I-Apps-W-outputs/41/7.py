
def solve(n, a):
    # Initialize the winner as the first player
    winner = "First"

    # Loop through each pile and check if the first player can make a move
    for i in range(n):
        # If the current pile has at least one stone, the first player can make a move
        if a[i] > 0:
            # Set the winner to the second player
            winner = "Second"
            break

    # Return the winner
    return winner

