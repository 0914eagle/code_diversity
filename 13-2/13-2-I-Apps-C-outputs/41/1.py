
def f1(N, A, K):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [A[i] for i in range(N)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [int(A[i] / K[i]) for i in range(N)]
    # Initialize the player who will make the next move
    player = 0
    # Initialize the number of moves made
    moves = 0
    # Loop until a player cannot make a move
    while True:
        # Get the index of the pile with the most stones
        max_index = num_stones.index(max(num_stones))
        # Get the maximum number of stones that can be removed from the selected pile
        max_stones[max_index] = int(num_stones[max_index] / K[max_index])
        # Remove the maximum number of stones from the selected pile
        num_stones[max_index] -= max_stones[max_index]
        # Update the number of moves made
        moves += 1
        # Check if a player cannot make a move
        if all(num_stones[i] == 0 for i in range(N)):
            break
        # Switch the player who will make the next move
        player = 1 - player
    # Return the winner of the game
    return "Takahashi" if player == 0 else "Aoki"

def f2(N, A, K):
    # Initialize the number of stones that can be removed from each pile
    num_stones = [A[i] for i in range(N)]
    # Initialize the maximum number of stones that can be removed from each pile
    max_stones = [int(A[i] / K[i]) for i in range(N)]
    # Initialize the player who will make the next move
    player = 0
    # Initialize the number of moves made
    moves = 0
    # Loop until a player cannot make a move
    while True:
        # Get the index of the pile with the most stones
        max_index = num_stones.index(max(num_stones))
        # Get the maximum number of stones that can be removed from the selected pile
        max_stones[max_index] = int(num_stones[max_index] / K[max_index])
        # Remove the maximum number of stones from the selected pile
        num_stones[max_index] -= max_stones[max_index]
        # Update the number of moves made
        moves += 1
        # Check if a player cannot make a move
        if all(num_stones[i] == 0 for i in range(N)):
            break
        # Switch the player who will make the next move
        player = 1 - player
    # Return the winner of the game
    return "Takahashi" if player == 0 else "Aoki"

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    K = list(map(int, input().split()))
    print(f1(N, A, K))
    print(f2(N, A, K))

