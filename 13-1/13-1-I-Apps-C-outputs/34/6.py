
def stone_taking_game(n, a, k):
    # Initialize the number of stones that can be taken from each pile
    num_stones = [a[i] for i in range(n)]
    # Initialize the maximum number of stones that can be taken from each pile
    max_stones = [int(a[i] / k[i]) for i in range(n)]
    # Initialize the turn player
    turn = 0
    # Initialize the winner
    winner = None
    # While there are still stones left in the game
    while any(num_stones):
        # Determine the current player
        player = turn % 2
        # Determine the number of stones that can be taken from each pile
        num_stones_taken = [min(max_stones[i], num_stones[i]) for i in range(n)]
        # Update the number of stones left in each pile
        num_stones = [num_stones[i] - num_stones_taken[i] for i in range(n)]
        # Update the maximum number of stones that can be taken from each pile
        max_stones = [int(max_stones[i] / k[i]) for i in range(n)]
        # Update the turn player
        turn += 1
        # If the current player has won the game
        if not any(num_stones):
            # Set the winner
            winner = player
            break
    # Return the winner
    return "Takahashi" if winner == 0 else "Aoki"

