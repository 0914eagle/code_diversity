
import sys

def count_ways(N, M, conditions):
    # Initialize the number of ways to paint the squares
    ways = 1
    
    # Iterate over each condition
    for i in range(M):
        # Get the left and right indices, and the number of different colors
        l, r, x = conditions[i]
        
        # Calculate the number of ways to paint the squares with the current condition
        num_ways = 0
        for j in range(l, r+1):
            num_ways += (N - j + 1) * (j - l + 1)
        
        # Update the number of ways to paint the squares
        ways *= num_ways
    
    # Return the result modulo 10^9+7
    return ways % 1000000007

if __name__ == '__main__':
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(count_ways(N, M, conditions))

