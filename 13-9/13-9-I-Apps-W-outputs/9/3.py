
def solve(k, n):
    count = 0
    while n > 0:
        if n % 10 < k:
            count += 1
        n //= 10
    return count

