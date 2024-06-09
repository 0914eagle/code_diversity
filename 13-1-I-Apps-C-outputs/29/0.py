
def solve(n, x):
    # Calculate the number of factors of each number
    factors = [0] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i, n + 1, i):
            factors[j] += 1
    
    # Initialize the dp table with the number of factors
    dp = [1] + [0] * n
    for i in range(1, n):
        dp[i] = (dp[i - 1] * factors[i]) % 1000000007
    
    # Calculate the number of ways to stretch the streamers
    result = 0
    for i in range(n):
        result = (result + dp[i]) % 1000000007
    
    return result

