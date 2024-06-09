
def brutality(hits, k):
    n = len(hits)
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - k - 1] + hits[i - 1])
    return dp[n]

def main():
    n, k = map(int, input().split())
    hits = list(map(int, input().split()))
    print(brutality(hits, k))

if __name__ == '__main__':
    main()

