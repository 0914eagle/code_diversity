
def f1(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and update the scores of the players
    for i in range(Q):
        scores[A[i] - 1] -= 1

    # Return True if the player survived, False otherwise
    return any(score > 0 for score in scores)

def f2(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and update the scores of the players
    for i in range(Q):
        scores[A[i] - 1] -= 1

    # Return the indices of the players who survived
    return [i + 1 for i, score in enumerate(scores) if score > 0]

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    print(f1(N, K, Q, A))
    print(f2(N, K, Q, A))

