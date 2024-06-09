
def get_maximum_sum(a, m):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 1] + a[i - 1])
    maximum_sum = 0
    for i in range(n, 0, -1):
        if dp[i] > maximum_sum:
            maximum_sum = dp[i]
        if maximum_sum > m:
            break
    return maximum_sum % m

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_sum(a, m))

if __name__ == '__main__':
    main()

