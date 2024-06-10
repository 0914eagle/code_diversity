
def get_number_of_ways(A, B):
    n = len(A)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] == B[j] and A[j] == B[i]:
                dp[i][j] = dp[i+1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i+1][j-1]
    return dp[0][n-1]

def main():
    A, B = input().split()
    print(get_number_of_ways(A, B))

if __name__ == '__main__':
    main()

