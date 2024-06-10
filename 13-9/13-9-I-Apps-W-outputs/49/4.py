
def get_maximum_gifts(a, s):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if a[j] <= s:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_maximum_gifts(a, s))

if __name__ == '__main__':
    main()

