
def get_number_of_ways(n, k, S, a):
    # Initialize a dictionary to store the results
    dp = {0: 1}
    
    # Iterate over the cubes
    for i in range(n):
        # Iterate over the possible numbers
        for j in range(1, S+1):
            # Check if the current number is available
            if j in dp:
                # If the current number is available, add the number of ways to choose this cube
                dp[j] += dp[j-a[i]]
    
    # Return the number of ways to choose the cubes and stick exclamation marks
    return dp[S]

def main():
    # Read the input
    n, k, S = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the function to get the number of ways
    result = get_number_of_ways(n, k, S, a)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

