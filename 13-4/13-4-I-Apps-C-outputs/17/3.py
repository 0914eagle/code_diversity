
import sys

def count_ways(N, M, conditions):
    # Initialize the number of ways to paint the squares
    ways = 1
    
    # Iterate over each condition
    for i in range(M):
        # Get the range of squares and the number of different colors
        l, r, x = conditions[i]
        N_colors = r - l + 1
        
        # Calculate the number of ways to paint the squares with x different colors
        ways *= comb(N_colors, x)
        
        # Calculate the number of ways to paint the squares with more than x different colors
        ways *= comb(N - N_colors + 1, M - i - 1)
    
    return ways % 1000000007

def comb(n, k):
    if k > n or k < 0:
        return 0
    if k == 0 or n == k:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)

if __name__ == '__main__':
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(count_ways(N, M, conditions))

