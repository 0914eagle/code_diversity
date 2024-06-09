
import sys

def get_input():
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    return N, M, conditions

def count_ways(N, M, conditions):
    # Initialize the dp table with all 1s
    dp = [1] * (N + 1)
    
    # Loop through the conditions and update the dp table
    for l, r, x in conditions:
        for i in range(l, r + 1):
            dp[i] = (dp[i] * x) % 1000000007
    
    # Return the result
    return sum(dp) % 1000000007

if __name__ == '__main__':
    N, M, conditions = get_input()
    print(count_ways(N, M, conditions))

