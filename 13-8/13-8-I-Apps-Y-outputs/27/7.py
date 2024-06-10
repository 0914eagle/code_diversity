
def get_good_times(a, l, r):
    good_times = 0
    current_time = 0
    for i in range(len(a)):
        if current_time + a[i] - 1 >= l and current_time + a[i] - 1 <= r:
            good_times += 1
        current_time += a[i]
    return good_times

def get_optimal_good_times(a, l, r):
    n = len(a)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if a[i - 1] > l:
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
        else:
            dp[i] = dp[i - 1]
    return dp[n]

if __name__ == '__main__':
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_optimal_good_times(a, l, r))

