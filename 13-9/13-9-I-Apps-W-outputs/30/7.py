
def get_number_of_ways(A, B):
    n = len(A)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if A[i] == B[j - 1]:
                dp[i][j] += dp[i + 1][j - 1]
            dp[i][j] += dp[i][j - 1]
    return dp[0][n]

def main():
    A = input()
    B = input()
    print(get_number_of_ways(A, B))

if __name__ == '__main__':
    main()

