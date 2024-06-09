
def find_lipschitz_constant(f):
    N = len(f)
    L = 0
    for i in range(N):
        for j in range(i+1, N):
            L = max(L, abs(f[i] - f[j]) / abs(i - j))
    return L

