
def stone_taking_game(n, a, k):
    # Initialize the number of stones that can be taken from each pile
    num_stones = [a[i] for i in range(n)]
    # Initialize the maximum number of stones that can be taken from each pile
    max_stones = [int(a[i] / k[i]) for i in range(n)]
    # Initialize the turn player
    turn = 0
    # Initialize the winner
    winner = None
    # Loop until a player can no longer make a move
    while True:
        # Get the current player
        player = turn % 2
        # Get the current pile
        pile = turn // 2
        # Check if the current player can make a move
        if num_stones[pile] > 0:
            # Get the number of stones that can be taken from the current pile
            num_stones_taken = min(max_stones[pile], num_stones[pile])
            # Update the number of stones in the current pile
            num_stones[pile] -= num_stones_taken
            # Update the maximum number of stones that can be taken from the current pile
            max_stones[pile] = int(num_stones[pile] / k[pile])
            # Update the turn player
            turn += 1
        else:
            # No more moves can be made, so the other player wins
            winner = 1 - player
            break
    
    # Return the winner
    return "Takahashi" if winner == 0 else "Aoki"

