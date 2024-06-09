
def is_valid_network(D):
    N = len(D)
    if N < 2:
        return "NO"
    for i in range(N):
        if D[i] > N - 1:
            return "NO"
    for i in range(N):
        if D[i] != 0 and D[i] != 1:
            return "NO"
    return "YES"

