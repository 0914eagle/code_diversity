
def solve(X):
    # Find the smallest k such that (Y1 + 1) * (Y2 + 1) * ... * (Yk + 1) = X
    k = 1
    while X > 1:
        X //= k + 1
        k += 1
    return k

