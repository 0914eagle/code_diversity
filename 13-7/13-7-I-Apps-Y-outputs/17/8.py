
def can_snuke_permute(sequence):
    N = len(sequence)
    if N < 2:
        return True
    if N % 2 == 1:
        return False
    for i in range(N // 2):
        if sequence[i] * sequence[N - 1 - i] % 4 != 0:
            return False
    return True

