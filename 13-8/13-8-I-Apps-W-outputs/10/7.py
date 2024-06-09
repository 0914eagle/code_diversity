
def solve(n, k, A, B):
    cost = 0
    while n > 1:
        if n % k == 0:
            cost += B
            n //= k
        else:
            cost += A
            n -= 1
    return cost

