
def stone_taking_game(n, a, k):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [a[i] for i in range(n)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [int(a[i] / k[i]) for i in range(n)]
    # Initialize the turn of the current player
    turn = 0
    # Initialize the winner of the game
    winner = None
    # Loop until a winner is determined
    while winner is None:
        # Determine the current player
        if turn % 2 == 0:
            player = "Takahashi"
        else:
            player = "Aoki"
        # Determine the pile that the current player will choose
        pile = 0
        # Loop until a valid pile is chosen
        while pile < 0 or pile >= n or num_stones[pile] == 0:
            # Ask the current player to choose a pile
            pile = int(input(f"{player}, choose a pile: "))
        # Determine the number of stones that the current player will remove from the chosen pile
        num_removed = 1
        # Loop until a valid number of stones is removed
        while num_removed < 1 or num_removed > max_stones[pile]:
            # Ask the current player to choose the number of stones to remove
            num_removed = int(input(f"{player}, choose the number of stones to remove: "))
        # Update the number of stones in the chosen pile
        num_stones[pile] -= num_removed
        # Update the maximum number of stones that can be removed from the chosen pile
        max_stones[pile] = int(num_stones[pile] / k[pile])
        # Update the turn of the current player
        turn += 1
        # Check if the game is over
        if num_stones[pile] == 0:
            # The current player has won the game
            winner = player
    # Return the winner of the game
    return winner

