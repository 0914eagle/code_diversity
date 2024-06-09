
def can_snuke_achieve_objective(sequence):
    n = len(sequence)
    if n < 2:
        return True
    if n % 2 == 1:
        return False
    for i in range(n // 2):
        if sequence[i] * sequence[n - i - 1] % 4 != 0:
            return False
    return True

