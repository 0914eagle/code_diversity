
def f1(n):
    for m in range(1, int(n**0.5) + 1):
        k = (n - m**2)**0.5
        if k == int(k):
            return m, int(k)
    return "impossible"

