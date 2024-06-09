
def can_snuke_permute(sequence):
    n = len(sequence)
    if n < 2:
        return True
    if n % 2 == 1:
        return False
    for i in range(n // 2):
        if sequence[i] * sequence[n - 1 - i] % 4 != 0:
            return False
    return True

