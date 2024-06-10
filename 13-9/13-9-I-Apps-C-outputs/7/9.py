
def solve(n, k):
    # Initialize the number of ways as 1
    ways = 1
    
    # Iterate over the houses
    for i in range(1, n + 1):
        # If the house is not the first house
        if i != 1:
            # If the house is indexed from 1 to k, inclusive
            if i <= k:
                # The penguin can walk to house number 1
                ways *= 2
            else:
                # The penguin cannot walk to house number 1
                ways *= 1
    
    # Return the number of ways modulo 1000000007
    return ways % 1000000007

def main():
    # Read the input
    n, k = map(int, input().split())
    
    # Call the solve function
    result = solve(n, k)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

