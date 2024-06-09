
def f1(N, A, K):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [A[i] for i in range(N)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [A[i] // K[i] for i in range(N)]
    # Initialize the player who will play next
    player = 0
    # Loop until a player cannot make a move
    while True:
        # Get the index of the pile that the current player can remove stones from
        i = player
        # Check if the current player can make a move
        if num_stones[i] > 0:
            # Calculate the number of stones that the current player can remove
            num_remove = min(num_stones[i], max_stones[i])
            # Remove the stones from the pile
            num_stones[i] -= num_remove
            # Update the maximum number of stones that can be removed from the pile
            max_stones[i] = num_stones[i] // K[i]
            # Switch to the other player
            player = 1 - player
        else:
            # If the current player cannot make a move, the other player wins
            return 1 - player

