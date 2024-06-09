
import sys

def modulo_combination(n, r, mod):
    if n == r == 0:
        return 1
    if r == 0:
        return 1
    if n == r:
        return 1
    if n == 0:
        return 0
    if r == 1:
        return n
    if n == 1:
        return 1
    return (modulo_combination(n-1, r, mod) + modulo_combination(n-1, r-1, mod)) % mod

def solve(a, c, m):
    total = a + c + m
    if total == 0:
        return 1
    if total == 1:
        return 1
    if total == 2:
        if a == 1 and c == 1:
            return 2
        if a == 1 and m == 1:
            return 2
        if c == 1 and m == 1:
            return 2
        return 1
    if a == 0:
        return modulo_combination(c+m, 2, 1000000007)
    if c == 0:
        return modulo_combination(a+m, 2, 1000000007)
    if m == 0:
        return modulo_combination(a+c, 2, 1000000007)
    return modulo_combination(a+c+m, 2, 1000000007) - modulo_combination(a, 2, 1000000007) * modulo_combination(c+m, 2, 1000000007) - modulo_combination(c, 2, 1000000007) * modulo_combination(a+m, 2, 1000000007) - modulo_combination(m, 2, 1000000007) * modulo_combination(a+c, 2, 1000000007) + modulo_combination(a, 2, 1000000007) * modulo_combination(c, 2, 1000000007) * modulo_combination(m, 2, 1000000007)

a, c, m = map(int, input().split())
print(solve(a, c, m))

