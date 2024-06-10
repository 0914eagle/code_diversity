
def get_input():
    n, k = map(int, input().split())
    strings = [input() for _ in range(n)]
    return n, k, strings

def longest_common_subsequence(strings):
    m = len(strings)
    n = len(strings[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if strings[i - 1][j - 1] == strings[0][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def main():
    n, k, strings = get_input()
    print(longest_common_subsequence(strings))

if __name__ == '__main__':
    main()

