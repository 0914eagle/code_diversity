
def get_minimum_steps(a, b):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(1, i + 1):
            if a[i - j] != b[i - j]:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[n]

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    print(get_minimum_steps(a, b))

if __name__ == '__main__':
    main()

