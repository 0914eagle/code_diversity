
import sys

def count_ways(N, M, conditions):
    # Initialize the number of ways to paint the squares
    ways = 1
    
    # Loop through each condition
    for l, r, x in conditions:
        # Calculate the number of ways to paint the squares within this range
        num_ways = (N - l + 1) * (N - r) // x
        ways *= num_ways
    
    # Return the number of ways modulo 10^9+7
    return ways % 1000000007

def main():
    # Read the input data
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    
    # Calculate the number of ways to paint the squares
    ways = count_ways(N, M, conditions)
    
    # Print the result
    print(ways)

if __name__ == '__main__':
    main()

