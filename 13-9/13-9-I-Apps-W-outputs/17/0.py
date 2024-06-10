
def count_subsequences(sequence, k):
    n = len(sequence)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = 1
    for i in range(2, n+1):
        for j in range(2, k+1):
            if sequence[i-1] == sequence[i-j]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1]
    return dp[n][k]

def main():
    n = int(input())
    sequence = [int(x) for x in input().split()]
    for k in range(1, n+1):
        print(count_subsequences(sequence, k))

if __name__ == '__main__':
    main()

