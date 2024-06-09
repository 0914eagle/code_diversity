
import sys

def solve(n, m, k, b):
    # Calculate the number of distinct strings modulo 998244353
    result = 1
    for i in range(m):
        result = (result * b[i]) % 998244353
    
    return result

n, m, k = map(int, input().split())
b = list(map(int, input().split()))
print(solve(n, m, k, b))

