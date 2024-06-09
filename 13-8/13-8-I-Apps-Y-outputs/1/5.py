
def is_valid_network(D):
    N = len(D)
    if N < 2:
        return "NO"
    for i in range(N):
        if D[i] < 0 or D[i] > N - 1:
            return "NO"
    for i in range(N):
        if D[i] == 0 and i != 0:
            return "NO"
    for i in range(N):
        if D[i] == N - 1 and i != N - 1:
            return "NO"
    for i in range(N):
        for j in range(i + 1, N):
            if D[i] == j - i and D[j] == i - j:
                return "NO"
    return "YES"

