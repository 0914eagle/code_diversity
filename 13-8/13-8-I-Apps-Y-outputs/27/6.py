
def get_good_sleeping_times(a, l, r):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if l <= a[i - 1] <= r:
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
        else:
            dp[i] = max(dp[i - 1], dp[i - 2])
    return dp[n]

def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_good_sleeping_times(a, l, r))

if __name__ == '__main__':
    main()

