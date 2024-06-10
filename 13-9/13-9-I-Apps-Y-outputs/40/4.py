
def get_optimal_position(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + 1)
            if s[i] != s[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1)
    return dp[0][n]

def get_optimal_substring(s, pos):
    n = len(s)
    l, r = 0, pos
    dp = [0] * (n + 1)
    for i in range(pos, -1, -1):
        if s[i] != s[pos]:
            l = i + 1
            break
    for i in range(pos + 1, n + 1):
        if s[i - 1] != s[pos]:
            r = i - 1
            break
    return s[l:r]

def main():
    n = int(input())
    s = input()
    pos = get_optimal_position(s)
    substring = get_optimal_substring(s, pos)
    print(len(set(substring)))

if __name__ == '__main__':
    main()

