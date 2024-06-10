
def count_incomparable_strings(s1, s2):
    n = len(s1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == '?':
                dp[i][j] += dp[i - 1][j]
            if s2[j - 1] == '?':
                dp[i][j] += dp[i][j - 1]
            if s1[i - 1] != '?' and s2[j - 1] != '?':
                if s1[i - 1] > s2[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += dp[i][j - 1]
    return dp[n][n]

def count_ways_to_replace_question_marks(s1, s2):
    n = len(s1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == '?':
                dp[i][j] += dp[i - 1][j]
            if s2[j - 1] == '?':
                dp[i][j] += dp[i][j - 1]
            if s1[i - 1] != '?' and s2[j - 1] != '?':
                if s1[i - 1] > s2[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += dp[i][j - 1]
    return dp[n][n]

def main():
    n = int(input())
    s1 = input()
    s2 = input()
    print(count_ways_to_replace_question_marks(s1, s2) % 1000000007)

if __name__ == '__main__':
    main()

