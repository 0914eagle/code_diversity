
def count_ways(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if s[i - 1] == '?':
            dp[i] += dp[i - 1]
        if i > 1 and s[i - 2] == '?':
            dp[i] += dp[i - 2]
        if i > 2 and s[i - 3] == '?':
            dp[i] += dp[i - 3]
        if s[i - 1].isdigit():
            dp[i] += dp[i - 1]
    return dp[n] % 1000000007

def main():
    s = input()
    print(count_ways(s))

if __name__ == '__main__':
    main()

