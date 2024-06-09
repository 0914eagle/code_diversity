
import math

def k_tree_paths(n, k, d):
    mod = 1000000007
    paths = 0
    
    for i in range(1, k+1):
        if i >= d:
            paths += math.comb(k, i) * math.comb(n-1, i-1)
    
    return paths % mod

