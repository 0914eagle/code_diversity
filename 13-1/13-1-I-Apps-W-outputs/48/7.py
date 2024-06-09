
def f1(n, k):
    # Find the smallest positive integer solution to (x div k) * (x mod k) = n
    x = 1
    while (x // k) * (x % k) != n:
        x += 1
    return x

