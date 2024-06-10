
def count_incomparable_strings(s1, s2):
    n = len(s1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == "?":
                dp[i][j] += dp[i - 1][j]
            if s2[j - 1] == "?":
                dp[i][j] += dp[i][j - 1]
            if s1[i - 1] != "?" and s2[j - 1] != "?":
                if s1[i - 1] > s2[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][n]

def count_incomparable_strings_with_templates(s1, s2):
    n = len(s1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == "?":
                dp[i][j] += dp[i - 1][j]
            if s2[j - 1] == "?":
                dp[i][j] += dp[i][j - 1]
            if s1[i - 1] != "?" and s2[j - 1] != "?":
                if s1[i - 1] > s2[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][n]

if __name__ == '__main__':
    n = int(input())
    s1 = input()
    s2 = input()
    count = count_incomparable_strings(s1, s2)
    count_with_templates = count_incomparable_strings_with_templates(s1, s2)
    print(count_with_templates % 1000000007)

