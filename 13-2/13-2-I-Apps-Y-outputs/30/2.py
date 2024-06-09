
def f1(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and decrease the score of all players except the one who answered correctly
    for i in range(Q):
        scores[A[i] - 1] -= 1
        for j in range(N):
            if j != A[i] - 1:
                scores[j] -= 1

    # Return the surviving players
    return [i + 1 for i in range(N) if scores[i] >= 0]

def f2(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and decrease the score of all players except the one who answered correctly
    for i in range(Q):
        scores[A[i] - 1] -= 1
        for j in range(N):
            if j != A[i] - 1:
                scores[j] -= 1

    # Return the surviving players
    return [i + 1 for i in range(N) if scores[i] >= 0]

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    print(*f1(N, K, Q, A), sep='\n')

