
def solve(n, k, sequence, costs):
    # Initialize a dictionary to store the minimum cost to make the sequence unbalanced
    dp = {0: 0}
    for i in range(1, n + 1):
        dp[i] = float('inf')
    for i in range(n):
        # Try changing the current position to '(' or ')'
        for j in range(i, n + 1):
            if j - i > k:
                break
            if sequence[i] == '(':
                dp[j] = min(dp[j], dp[i] + costs[i])
            else:
                dp[j] = min(dp[j], dp[i] - costs[i])
    # Return the minimum cost to make the sequence unbalanced
    return dp[n]

