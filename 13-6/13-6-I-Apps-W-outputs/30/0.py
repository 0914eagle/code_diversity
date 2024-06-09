
def max_sum_modulo(a, m):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i - 1])
    return dp[n] % m

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_sum_modulo(a, m))

if __name__ == '__main__':
    main()

