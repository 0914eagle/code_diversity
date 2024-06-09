
import sys

def g_n(x, n, A, B):
    if n == 0:
        return x
    else:
        return (A * g_n(x, n-1, A, B) + B) % 1000000007

A, B, n, x = map(int, input().split())
print(g_n(x, n, A, B))

