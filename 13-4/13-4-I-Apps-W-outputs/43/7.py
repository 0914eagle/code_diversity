
def solve(n, k):
    count = 0
    while n > 0:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        count += 1
    return count

