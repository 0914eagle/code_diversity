
def get_number_of_ways(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if s[i - 1] == '?':
            dp[i] += dp[i - 1]
        elif s[i - 1] == '*':
            if i > 1 and s[i - 2] in '012':
                dp[i] += dp[i - 2]
            if i < n and s[i] in '012':
                dp[i] += dp[i - 1]
        else:
            if i > 1 and s[i - 2] in '012':
                dp[i] += dp[i - 2]
            if i < n and s[i] in '012':
                dp[i] += dp[i - 1]
    return dp[n] % 1000000007

def main():
    s = input()
    print(get_number_of_ways(s))

if __name__ == '__main__':
    main()

