
def solve(n):
    for m in range(2, n):
        if n % m == 0:
            continue
        if is_squarefree(m * n):
            return m
    return -1

def is_squarefree(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

