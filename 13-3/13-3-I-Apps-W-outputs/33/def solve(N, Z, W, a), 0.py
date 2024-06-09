
def solve(N, Z, W, a):
    # X will play the game so that the score will be maximized
    # Y will play the game so that the score will be minimized
    # We can use dynamic programming to solve this problem
    # dp[i] will store the maximum score that X can get when there are i cards left in the deck
    # dp[i] = max(dp[i-1], dp[i-2] + a[i-1])
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = a[0]
    for i in range(2, N+1):
        dp[i] = max(dp[i-1], dp[i-2] + a[i-1])
    # print(dp)
    return abs(dp[N] - W)

