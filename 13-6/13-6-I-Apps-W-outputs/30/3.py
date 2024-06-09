
def get_max_sum(a, m):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 1] + a[i - 1])
    max_sum = 0
    for i in range(n, 0, -1):
        if dp[i] > max_sum:
            max_sum = dp[i]
        if max_sum > m:
            return max_sum % m
    return max_sum

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_sum(a, m))

if __name__ == '__main__':
    main()

