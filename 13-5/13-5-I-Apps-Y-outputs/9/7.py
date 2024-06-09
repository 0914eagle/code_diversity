
def get_max_problems(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if a[i - 1] >= 2 * a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_problems(a))

if __name__ == '__main__':
    main()

