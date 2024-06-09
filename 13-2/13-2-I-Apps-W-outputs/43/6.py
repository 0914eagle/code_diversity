
def count_setlists(hype_ratings):
    n = len(hype_ratings)
    if n < 3:
        return 0
    
    # Initialize the dp table with all values set to 0
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # Iterate over the hype ratings and calculate the number of setlists
    for i in range(1, n + 1):
        if hype_ratings[i - 1] == 1:
            dp[i] += dp[i - 1]
        if hype_ratings[i - 1] == 2:
            dp[i] += dp[i - 2]
        if hype_ratings[i - 1] == 3:
            dp[i] += dp[i - 3]
    
    # Return the number of setlists modulo 10^9 + 7
    return dp[n] % 1000000007

if __name__ == '__main__':
    n = int(input())
    hype_ratings = list(map(int, input().split()))
    print(count_setlists(hype_ratings))

