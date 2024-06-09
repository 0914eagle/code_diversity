
def f1(N, A, K):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [A[i] for i in range(N)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [int(A[i] / K[i]) for i in range(N)]
    # Initialize the player who will make the next move
    player = 0
    # Initialize the number of moves made
    moves = 0
    # Loop until a player can no longer make a move
    while True:
        # Get the index of the pile with the maximum number of stones
        max_index = num_stones.index(max(num_stones))
        # Get the maximum number of stones that can be removed from the selected pile
        max_stones_removed = min(max_stones[max_index], num_stones[max_index])
        # Remove the maximum number of stones from the selected pile
        num_stones[max_index] -= max_stones_removed
        # Update the maximum number of stones that can be removed from each pile
        max_stones = [int(num_stones[i] / K[i]) for i in range(N)]
        # Switch the player
        player = 1 - player
        # Increment the number of moves made
        moves += 1
        # If a player cannot make a move, the game is over
        if max(num_stones) == 0:
            break
    # If the number of moves is even, the first player wins
    if moves % 2 == 0:
        return "Takahashi"
    # If the number of moves is odd, the second player wins
    else:
        return "Aoki"

def f2(...):
    ...

if __name__ == '__main__':
    ...

