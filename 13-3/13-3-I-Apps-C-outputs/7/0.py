
import sys

def count_ways(N, M, conditions):
    # Initialize the number of ways to paint the squares
    ways = 1
    
    # Loop through each condition
    for i in range(M):
        # Get the range of squares and the number of different colors
        l, r, x = conditions[i]
        # Calculate the number of ways to paint the squares in this range
        ways *= (r - l + 1) * (x - 1)
        # Reduce the number of ways modulo 10^9+7
        ways %= 1000000007
    
    # Return the number of ways to paint the squares
    return ways

def main():
    # Read the input data
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    
    # Calculate the number of ways to paint the squares
    ways = count_ways(N, M, conditions)
    
    # Print the result
    print(ways)

if __name__ == '__main__':
    main()

