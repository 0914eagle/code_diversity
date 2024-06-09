
def get_max_score(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n + 1):
            if j == i:
                dp[i][j] = a[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1] + a[j - 1], dp[i + 1][j] + a[i - 1])
    return dp[0][n]

def get_optimal_segment(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n + 1):
            if j == i:
                dp[i][j] = a[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1] + a[j - 1], dp[i + 1][j] + a[i - 1])
    max_score = dp[0][n]
    optimal_segment = []
    i = 0
    j = n
    while i < j:
        if dp[i][j] == dp[i][j - 1] + a[j - 1]:
            optimal_segment.append(j)
            j -= 1
        else:
            optimal_segment.append(i)
            i += 1
    return optimal_segment, max_score

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_score(a))
    print(*get_optimal_segment(a)[0], sep=' ')

