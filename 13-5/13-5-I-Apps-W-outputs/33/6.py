
def get_max_score(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = cards[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + cards[j - 1])
    return dp[n][n]

def get_optimal_segment(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = cards[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + cards[j - 1])
    opt_segment = []
    i, j = n, n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            opt_segment.append(j)
            i -= 1
            j -= 1
    opt_segment.reverse()
    return opt_segment

def main():
    n = int(input())
    cards = [int(x) for x in input().split()]
    print(get_max_score(cards))
    print(get_optimal_segment(cards))

if __name__ == '__main__':
    main()

