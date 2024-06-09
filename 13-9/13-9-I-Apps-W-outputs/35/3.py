
def solve(a, b, c):
    return sum(i * j * k for i in range(1, a + 1) for j in range(1, b + 1) for k in range(1, c + 1)) % 998244353

