
import sys

def count_ways(N, M, conditions):
    # Initialize the number of ways to paint the squares
    ways = 1
    
    # Loop through each condition
    for i in range(M):
        # Get the left and right indices, and the number of different colors required
        l, r, x = conditions[i]
        
        # Calculate the number of ways to paint the squares with the current condition
        num_ways = 0
        for j in range(l-1, r):
            # If the current square is not painted, add the number of ways to paint it with the current condition
            if j not in painted:
                num_ways += x
        
        # Multiply the number of ways to paint the current condition by the total number of ways to paint the previous conditions
        ways *= num_ways
    
    # Return the total number of ways to paint the squares
    return ways % 1000000007

def main():
    # Read the input data
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    
    # Call the count_ways function and print the result
    print(count_ways(N, M, conditions))

if __name__ == '__main__':
    main()

