
def get_max_gifts(a, s):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if a[i - 1] + dp[i - j] > dp[i]:
                dp[i] = a[i - 1] + dp[i - j]
    for i in range(n, 0, -1):
        if dp[i] <= s:
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

