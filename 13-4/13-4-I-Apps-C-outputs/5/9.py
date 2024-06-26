
def get_min_coins(s, a, b):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + a
        for j in range(1, i):
            if s[i - j:i] == s[:j]:
                dp[i] = min(dp[i], dp[j - 1] + b)
    return dp[n]

def main():
    n, a, b = map(int, input().split())
    s = input()
    print(get_min_coins(s, a, b))

if __name__ == '__main__':
    main()

