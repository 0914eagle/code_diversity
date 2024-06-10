
def get_max_gifts(a, s):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i - 1])
    for i in range(n - 1, -1, -1):
        if dp[i] + a[i] > s:
            return i
    return 0

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_max_gifts(a, s))

if __name__ == '__main__':
    main()

