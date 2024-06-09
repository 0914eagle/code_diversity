
import sys

def count_ways(N, M, conditions):
    # Initialize the number of ways to paint the squares
    ways = 1
    
    # Loop through each condition
    for i in range(M):
        # Get the left and right indices, and the number of different colors
        l, r, x = conditions[i]
        
        # Calculate the number of ways to paint the squares with the current condition
        num_ways = (r - l + 1) * (x - 1)
        
        # Update the number of ways to paint the squares
        ways = (ways * num_ways) % 1000000007
    
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

