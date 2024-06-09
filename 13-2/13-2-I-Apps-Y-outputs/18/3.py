
def get_max_prettiness(a):
    
    a.sort(reverse=True)
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return a[0] + a[1]
    if len(a) == 3:
        return max(a[0] + a[1], a[1] + a[2], a[0] + a[2])
    # If there are more than 3 problems, we need to find the maximum possible cumulative prettiness by considering all possible combinations of 3 problems.
    # We can use a dynamic programming approach to solve this problem.
    dp = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i - 1], dp[i - 3] + a[i - 2] + a[i - 1])
    return dp[-1]

