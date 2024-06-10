
def longest_exploration_sequence(arr, d, m):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, max(0, i - d - 1), -1):
            if abs(arr[i - 1] - arr[j]) <= m:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

def main():
    n, d, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(longest_exploration_sequence(arr, d, m))

if __name__ == '__main__':
    main()

