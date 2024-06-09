
def solve(n, z, w, a):
    # X will play the game so that the score will be maximized
    # Y will play the game so that the score will be minimized
    # We can use dynamic programming to solve this problem
    # Let dp[i] be the maximum score that X can get when there are i cards left in the deck
    # Let dp2[i] be the minimum score that Y can get when there are i cards left in the deck
    # Base case: dp[0] = 0, dp2[0] = 0
    dp = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    dp[0] = 0
    dp2[0] = 0
    for i in range(1, n + 1):
        # X will draw the maximum number of cards that he can
        # Y will draw the minimum number of cards that he can
        x_score = max(z + a[i - 1], dp[i - 1])
        y_score = min(w + a[i - 1], dp2[i - 1])
        dp[i] = x_score
        dp2[i] = y_score
    return abs(dp[n] - dp2[n])

