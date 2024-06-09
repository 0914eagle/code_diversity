
def solve(n, k, seq, costs):
    # Initialize a dictionary to store the minimum effort required to make the sequence unbalanced
    dp = {0: 0}
    for i in range(1, n + 1):
        dp[i] = float('inf')
    for i in range(n):
        # Try changing the current position to ')'
        if seq[i] == '(':
            if i + 1 <= k:
                dp[i + 1] = min(dp[i + 1], dp[i] + costs[i])
        # Try changing the current position to '('
        if seq[i] == ')':
            if i - 1 >= 0 and dp[i - 1] != float('inf'):
                dp[i] = min(dp[i], dp[i - 1] + costs[i - 1])
    # If Bruce can always rebalance the sequence, return '?'
    if dp[n] != float('inf'):
        return '?'
    # Otherwise, return the minimum effort required to make the sequence unbalanced
    return dp[n]

