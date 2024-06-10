
def get_min_operations(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(1, i):
            if s[i - j] == s[i - j - 1]:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[n]

def main():
    n = int(input())
    s = input()
    print(get_min_operations(s))

if __name__ == '__main__':
    main()

