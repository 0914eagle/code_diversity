
def max_score(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + cards[j - 1])
    return dp[n][n]

def min_score(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] - cards[j - 1])
    return dp[n][n]

def solve(cards):
    return max_score(cards), min_score(cards)

if __name__ == '__main__':
    n = int(input())
    cards = list(map(int, input().split()))
    print(solve(cards))

