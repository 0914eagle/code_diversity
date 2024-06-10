
def get_minimum_steps(a, b):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if a[j] == b[i - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

def main():
    n = int(input())
    a = [0] * n
    b = list(map(int, input().split()))
    print(get_minimum_steps(a, b))

if __name__ == '__main__':
    main()

