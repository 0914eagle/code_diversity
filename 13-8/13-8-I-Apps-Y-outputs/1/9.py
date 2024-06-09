
def is_valid_network(D):
    N = len(D)
    if N < 2:
        return "NO"
    for i in range(N):
        if D[i] > N - 1:
            return "NO"
    for i in range(N):
        if D[i] == 0:
            return "NO"
    for i in range(N):
        for j in range(i + 1, N):
            if D[i] > D[j]:
                return "NO"
    return "YES"
