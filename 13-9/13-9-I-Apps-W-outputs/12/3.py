
import sys

def k_tree_paths(n, k, d):
    mod = 1000000007
    paths = 0
    for i in range(1, k+1):
        if i >= d:
            paths += comb(n-1, k-1)
        paths %= mod
    return paths

def comb(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    return (comb(n-1, k-1) + comb(n-1, k)) % (1000000007)

n, k, d = map(int, sys.stdin.readline().split())
print(k_tree_paths(n, k, d))

