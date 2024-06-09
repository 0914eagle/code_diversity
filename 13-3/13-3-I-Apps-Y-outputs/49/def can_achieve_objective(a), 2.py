
def can_achieve_objective(a):
    N = len(a)
    if N < 2:
        return True
    if N % 2 == 1:
        return False
    for i in range(N // 2):
        if a[i] % 4 != 0 or a[N - 1 - i] % 4 != 0:
            return False
    return True
