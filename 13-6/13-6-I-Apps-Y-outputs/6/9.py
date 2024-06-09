
def get_satisfaction_points(N, A, B, C):
    satisfaction_points = 0
    for i in range(N):
        satisfaction_points += B[i]
        if i < N - 1 and A[i] == A[i + 1] - 1:
            satisfaction_points += C[i]
    return satisfaction_points

