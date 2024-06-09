
def solve(n, k, seq, costs):
    # Initialize a dictionary to store the minimum effort required to make the sequence unbalanced
    dp = {0: 0}
    for i in range(1, n + 1):
        dp[i] = float('inf')
    for i in range(n):
        # Try changing the current position to ')'
        if seq[i] == '(':
            if i + 1 not in dp or dp[i + 1] > dp[i] + costs[i]:
                dp[i + 1] = dp[i] + costs[i]
        # Try changing the current position to '('
        if seq[i] == ')':
            if i - 1 not in dp or dp[i - 1] > dp[i] + costs[i]:
                dp[i - 1] = dp[i] + costs[i]
    # If Bruce can rebalance the sequence in k moves or less, return -1
    if k >= n or any(dp[i] <= k for i in range(n + 1)):
        return -1
    # Otherwise, return the minimum effort required to make the sequence unbalanced
    return min(dp[i] for i in range(n + 1) if i not in dp)

