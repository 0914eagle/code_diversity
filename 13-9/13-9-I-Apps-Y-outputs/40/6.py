
def get_optimal_position(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]

def get_largest_common_substring(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] > result:
                result = dp[i][j]
    return result

def main():
    n = int(input())
    s = input()
    optimal_position = get_optimal_position(s)
    largest_common_substring = get_largest_common_substring(s)
    print(optimal_position)
    print(largest_common_substring)

if __name__ == '__main__':
    main()

