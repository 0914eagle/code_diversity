
def solve(n, x):
    # Calculate the number of factors of each number
    factors = [0] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i, n + 1, i):
            factors[j] += 1
    
    # Initialize the dp table with the number of factors
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = factors[i] * dp[i - 1]
    
    # Calculate the number of ways to stretch the streamers
    total = 0
    for i in range(n):
        total += dp[x[i]]
    
    # Return the result modulo 10^9 + 7
    return total % 1000000007

