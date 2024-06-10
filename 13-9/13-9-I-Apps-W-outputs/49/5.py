
def get_max_presents(a, s):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, min(i, s + 1)):
            dp[i] = max(dp[i], dp[i - j] + j)
    return dp[n]

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_max_presents(a, s))

if __name__ == '__main__':
    main()

