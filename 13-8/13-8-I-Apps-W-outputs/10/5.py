
def solve(n, k, A, B):
    coins = 0
    while n > 1:
        if n % k == 0:
            coins += B
            n //= k
        else:
            coins += A
            n -= 1
    return coins

