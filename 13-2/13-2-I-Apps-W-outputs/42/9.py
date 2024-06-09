
def f1(n):
    for m in range(1, n):
        k = n**2 - m**2
        if k > m and k % 2 == 0:
            return [m, int(k/2)]
    return [-1, -1]

