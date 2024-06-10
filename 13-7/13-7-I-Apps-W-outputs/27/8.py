
def get_number_of_ways(n, k, S, a):
    # Initialize a dictionary to store the results
    dp = {}
    
    # Base case: if S is 0, there is only one way to do it
    dp[0] = 1
    
    # Iterate over the given numbers
    for i in range(n):
        # Iterate over the possible number of stickers
        for j in range(k+1):
            # If the current number is less than or equal to S, we can choose it
            if a[i] <= S:
                # Add the number of ways to choose the current number and stick j exclamation marks to the result
                dp[S] += dp[S-a[i]]
    
    return dp[S]

def main():
    n, k, S = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_number_of_ways(n, k, S, a))

if __name__ == '__main__':
    main()

