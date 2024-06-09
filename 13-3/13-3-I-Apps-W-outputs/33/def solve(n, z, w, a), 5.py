
def solve(n, z, w, a):
    # X will play the game so that the score will be maximized
    # Y will play the game so that the score will be minimized
    # We can use dynamic programming to solve this problem
    # Let dp be a 2D array of size (n + 1) x (z + 1)
    # dp[i][j] represents the maximum score that X can get when there are i cards left in the deck and X has j points
    # Base case: dp[0][j] = 0 for all j, since there are no cards left in the deck
    # Base case: dp[i][0] = 0 for all i, since X has no points initially
    dp = [[0 for _ in range(z + 1)] for _ in range(n + 1)]

    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, z + 1):
            # If X draws the last card, the score will be j - a[i]
            dp[i][j] = max(dp[i - 1][j - a[i]], dp[i - 1][j] + a[i])

    # The score of the game is the absolute difference of the integers written on the cards in the two players' hand
    return abs(dp[n][z] - w)

