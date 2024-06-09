
import sys

def modulo_combination(n, r, mod):
    # Calculate the binomial coefficient (n choose r) modulo mod
    if r > n:
        return 0
    if r == 0:
        return 1
    if r == n:
        return 1
    if r == 1 or r == n - 1:
        return n
    
    # Calculate the value of (n * (n-1) * ... * (n-r+1)) modulo mod
    value = 1
    for i in range(n-r+1, n+1):
        value = value * i % mod
    
    # Calculate the value of (1 * 2 * ... * r) modulo mod
    denom = 1
    for i in range(1, r+1):
        denom = denom * i % mod
    
    return value * pow(denom, mod-2, mod) % mod

def solve(A, C, M):
    # Calculate the total number of boxes
    total = A + C + M
    
    # Calculate the number of ways to arrange the boxes with different types of fruits
    num_ways = 1
    for i in range(1, total):
        num_ways = num_ways * modulo_combination(total-i, i, 1000000007) % 1000000007
    
    return num_ways

if __name__ == "__main__":
    A, C, M = map(int, input().split())
    print(solve(A, C, M))

