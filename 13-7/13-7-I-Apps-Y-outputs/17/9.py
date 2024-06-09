
def can_snuke_achieve_objective(a):
    n = len(a)
    if n < 2:
        return True
    if a[0] % 4 != 0 or a[n-1] % 4 != 0:
        return False
    for i in range(1, n-1):
        if a[i] % 4 != 0 or a[i+1] % 4 != 0:
            return False
    return True

