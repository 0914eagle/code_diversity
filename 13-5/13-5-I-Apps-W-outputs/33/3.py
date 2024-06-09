
def get_max_score(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = cards[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + cards[i - 1], dp[i - 1][j] + cards[i - 1])
    return dp[n][n]

def get_optimal_segment(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = cards[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + cards[i - 1], dp[i - 1][j] + cards[i - 1])
    max_score = dp[n][n]
    optimal_segment = []
    i, j = n, n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - 1] + cards[i - 1]:
            optimal_segment.append(i)
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + cards[i - 1]:
            i -= 1
        else:
            j -= 1
    optimal_segment.reverse()
    return optimal_segment, max_score

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    optimal_segment, max_score = get_optimal_segment(cards)
    print(max_score)

if __name__ == '__main__':
    main()

