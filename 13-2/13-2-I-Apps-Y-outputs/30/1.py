
def f1(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and update the scores of the players
    for i in range(Q):
        scores[A[i] - 1] -= 1

    # Check which players survived the game
    survived = [False] * N
    for i in range(N):
        if scores[i] > 0:
            survived[i] = True

    return survived

def f2(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and update the scores of the players
    for i in range(Q):
        scores[A[i] - 1] -= 1

    # Check which players survived the game
    survived = []
    for i in range(N):
        if scores[i] > 0:
            survived.append(i + 1)

    return survived

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    print(*f1(N, K, Q, A), sep='\n')
    print(*f2(N, K, Q, A), sep='\n')

