
def get_max_divisible_by_3(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i - 1] + 1) if s[i] == '3' else dp[i]
    return dp[n]

def main():
    s = input()
    print(get_max_divisible_by_3(s))

if __name__ == '__main__':
    main()

