
def f1(n, k):
    while k > 0:
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10
        k -= 1
    return n

