
def f1(N, A, K):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [A[i] for i in range(N)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [A[i] // K[i] for i in range(N)]
    # Initialize the current player
    current_player = 0
    # Initialize the number of turns
    num_turns = 0
    # Loop until a player can no longer make a move
    while True:
        # Get the index of the pile with the most stones
        max_index = num_stones.index(max(num_stones))
        # Get the number of stones that can be removed from the pile with the most stones
        num_remove = min(max_stones[max_index], num_stones[max_index])
        # Remove the stones from the pile with the most stones
        num_stones[max_index] -= num_remove
        # Update the maximum number of stones that can be removed from each pile
        max_stones = [max(num_stones[i] // K[i], 0) for i in range(N)]
        # Switch to the other player
        current_player = 1 - current_player
        # Increment the number of turns
        num_turns += 1
        # If a player cannot make a move, the game is over
        if all(num_stones[i] == 0 for i in range(N)):
            break
    # If the game is over, return the winner
    if current_player == 0:
        return "Takahashi"
    else:
        return "Aoki"

def f2(N, A, K):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [A[i] for i in range(N)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [A[i] // K[i] for i in range(N)]
    # Initialize the current player
    current_player = 0
    # Initialize the number of turns
    num_turns = 0
    # Loop until a player can no longer make a move
    while True:
        # Get the index of the pile with the most stones
        max_index = num_stones.index(max(num_stones))
        # Get the number of stones that can be removed from the pile with the most stones
        num_remove = min(max_stones[max_index], num_stones[max_index])
        # Remove the stones from the pile with the most stones
        num_stones[max_index] -= num_remove
        # Update the maximum number of stones that can be removed from each pile
        max_stones = [max(num_stones[i] // K[i], 0) for i in range(N)]
        # Switch to the other player
        current_player = 1 - current_player
        # Increment the number of turns
        num_turns += 1
        # If a player cannot make a move, the game is over
        if all(num_stones[i] == 0 for i in range(N)):
            break
    # If the game is over, return the winner
    if current_player == 0:
        return "Takahashi"
    else:
        return "Aoki"

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    K = list(map(int, input().split()))
    print(f1(N, A, K))
    print(f2(N, A, K))

