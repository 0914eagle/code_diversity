
def f1(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and decrease the score of all players by 1
    for i in range(Q):
        scores[A[i] - 1] -= 1

    # Check which players survived the game
    survived = [score >= 0 for score in scores]

    return survived

def f2(N, K, Q, A):
    # Initialize the scores of all players to K
    scores = [K] * N

    # Loop through each correct answer and decrease the score of all players by 1
    for i in range(Q):
        scores[A[i] - 1] -= 1

    # Check which players survived the game
    survived = []
    for i in range(N):
        if scores[i] >= 0:
            survived.append("Yes")
        else:
            survived.append("No")

    return survived

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    print(*f1(N, K, Q, A), sep='\n')
    print(*f2(N, K, Q, A), sep='\n')

