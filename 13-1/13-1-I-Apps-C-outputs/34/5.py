
def stone_taking_game(n, a, k):
    # Initialize the number of stones that can be taken from each pile
    num_stones = [a[i] for i in range(n)]
    # Initialize the maximum number of stones that can be taken from each pile
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
        # Determine the pile that the current player will take stones from
        pile = turn // 2
        # Determine the number of stones that the current player can take from the current pile
        num_stones_taken = min(max_stones[pile], num_stones[pile])
        # Update the number of stones that can be taken from the current pile
        num_stones[pile] -= num_stones_taken
        # Update the maximum number of stones that can be taken from the current pile
        max_stones[pile] = int(num_stones[pile] / k[pile])
        # Check if the current player has won the game
        if num_stones[pile] == 0:
            winner = player
        # Update the turn of the current player
        turn += 1
    # Return the winner of the game
    return winner

