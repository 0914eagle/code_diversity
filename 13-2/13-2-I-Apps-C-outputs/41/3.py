
def f1(N, A, K):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [A[i] for i in range(N)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [int(A[i] / K[i]) for i in range(N)]
    # Initialize the player who will make the next move
    player = 0
    # Loop until a player cannot make a move
    while True:
        # Get the index of the pile from which the player will remove stones
        i = player
        # Get the number of stones that can be removed from the selected pile
        num_removable_stones = num_stones[i]
        # Get the maximum number of stones that can be removed from the selected pile
        max_removable_stones = max_stones[i]
        # If the player can remove at least one stone, remove the maximum number of stones
        if num_removable_stones > 0:
            num_stones[i] -= max_removable_stones
        # Update the player who will make the next move
        player = 1 - player
        # If a player cannot make a move, the game is over
        if num_stones[player] == 0:
            break
    # Return the winner of the game
    return "Takahashi" if player == 0 else "Aoki"

