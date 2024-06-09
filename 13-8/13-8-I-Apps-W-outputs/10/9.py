
def solve(n, k, A, B):
    count = 0
    while n > 1:
        if n % k == 0:
            n //= k
            count += B
        else:
            n -= 1
            count += A
    return count

