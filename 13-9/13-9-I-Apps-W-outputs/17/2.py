
def get_subsequences(sequence, k):
    n = len(sequence)
    mod = 1000000007
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j == 1:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
    return dp[n][k]

def solve(sequence):
    n = len(sequence)
    result = []
    for k in range(1, n+1):
        result.append(get_subsequences(sequence, k))
    return result

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    result = solve(sequence)
    for i in result:
        print(i)

