
def get_minimal_cut(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '0':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            dp[i] = max(dp[i], dp[i + 1] + 1)
    return dp[0]

def get_minimal_cut_strings(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '0':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            dp[i] = max(dp[i], dp[i + 1] + 1)
    strings = []
    i, j = 0, 0
    while i < n:
        if dp[i] == dp[i + 1]:
            strings.append(s[i:i + dp[i]])
            i += dp[i]
        else:
            strings.append(s[i])
            i += 1
    return strings

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(get_minimal_cut(s))
    print(' '.join(get_minimal_cut_strings(s)))

