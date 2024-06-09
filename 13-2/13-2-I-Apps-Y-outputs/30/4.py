
def f1(N, K, Q, A):
    # Initialize the scores of each player to K
    scores = [K] * N

    # Loop through each correct answer and subtract 1 point from the scores of all players except the one who answered correctly
    for i in range(Q):
        scores[A[i] - 1] -= 1
        for j in range(N):
            if j != A[i] - 1:
                scores[j] -= 1

    # Return True if the player survived, False otherwise
    return [scores[i] >= 0 for i in range(N)]

def f2(...):
    ...

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    print(*f1(N, K, Q, A), sep='\n')

