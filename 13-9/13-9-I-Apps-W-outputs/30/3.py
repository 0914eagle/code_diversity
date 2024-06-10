
def get_number_of_ways(A, B):
    n = len(A)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, -1, -1):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[n][0]

def main():
    A, B = input().split()
    print(get_number_of_ways(A, B))

if __name__ == '__main__':
    main()

