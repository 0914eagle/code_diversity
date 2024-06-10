
def get_num_ways(N, K):
    # Base case: if there is only one ball, there is only one way to paint it
    if N == 1:
        return K
    
    # Initialize the number of ways to paint the balls
    num_ways = 0
    
    # Iterate over all possible colors for the first ball
    for color1 in range(K):
        # Get the number of ways to paint the remaining balls with the current color of the first ball
        num_ways_remaining = get_num_ways(N-1, K)
        
        # Add the number of ways to paint the remaining balls to the total number of ways
        num_ways += num_ways_remaining
    
    return num_ways

def main():
    # Read the input from stdin
    N, K = map(int, input().split())
    
    # Call the function to get the number of ways to paint the balls
    num_ways = get_num_ways(N, K)
    
    # Print the result
    print(num_ways)

if __name__ == '__main__':
    main()

