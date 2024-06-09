
def f1(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer given by a player
    for i in range(Q):
        # Decrement the score of all players except the player who gave the correct answer
        for j in range(N):
            if j != A[i] - 1:
                scores[j] -= 1

    # Return True if a player has survived the game, False otherwise
    return any(score > 0 for score in scores)

def f2(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer given by a player
    for i in range(Q):
        # Decrement the score of all players except the player who gave the correct answer
        for j in range(N):
            if j != A[i] - 1:
                scores[j] -= 1

    # Return the indices of the players who have survived the game
    return [i + 1 for i in range(N) if scores[i] > 0]

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    print(*f1(N, K, Q, A), sep='\n')
    print(*f2(N, K, Q, A), sep='\n')

