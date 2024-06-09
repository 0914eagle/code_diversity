
import sys

def modulo_combination(n, k, mod):
    if n == k or k == 0:
        return 1
    if k == 1:
        return n
    if k == n - 1:
        return n * (n - 1) // 2
    return (modulo_combination(n - 1, k, mod) + modulo_combination(n - 1, k - 1, mod)) % mod

def solve(a, c, m):
    total = a + c + m
    if total % 2 == 1:
        return 0
    half = total // 2
    return modulo_combination(half, a, 1000000007) * modulo_combination(half, c, 1000000007) * modulo_combination(half, m, 1000000007) % 1000000007

a, c, m = map(int, input().split())
print(solve(a, c, m))

