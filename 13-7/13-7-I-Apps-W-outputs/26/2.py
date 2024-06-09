
def solve(a, m):
    count = 0
    for x in range(m):
        if a % m == gcd(a + x, m):
            count += 1
    return count

