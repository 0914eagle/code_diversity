
def get_max_score(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n + 1):
            if j == i:
                dp[i][j] = cards[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1] + cards[j - 1], dp[i][j - 2] + cards[j - 2])
    return dp[0][n]

def get_optimal_segment(cards):
    n = len(cards)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n + 1):
            if j == i:
                dp[i][j] = cards[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1] + cards[j - 1], dp[i][j - 2] + cards[j - 2])
    optimal_segment = []
    i = 0
    j = n
    while i < j:
        if dp[i][j] == dp[i][j - 1] + cards[j - 1]:
            optimal_segment.append(j)
            j -= 1
        else:
            optimal_segment.append(i)
            i += 1
    return optimal_segment

def main():
    n = int(input())
    cards = [int(x) for x in input().split()]
    print(get_max_score(cards))
    print(get_optimal_segment(cards))

if __name__ == '__main__':
    main()

