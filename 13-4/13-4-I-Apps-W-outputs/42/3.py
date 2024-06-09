
def get_cost(a, b):
    if a == b:
        return 0
    else:
        return c[a, b]

def solve(H, W, c, A):
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            if A[i][j] == -1:
                continue
            dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + get_cost(A[i][j], 1)
            for k in range(j):
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][k + 1] + dp[i + 1][j] + get_cost(A[i][j], A[i][k]))
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][k + 1] + dp[i + 1][j] + get_cost(A[i][j], A[i][k]))
    return dp[H][W]

def main():
    H, W = map(int, input().split())
    c = [[0] * 10 for _ in range(10)]
    for i in range(10):
        c[i] = list(map(int, input().split()))
    A = [[]] * H
    for i in range(H):
        A[i] = list(map(int, input().split()))
    print(solve(H, W, c, A))

if __name__ == '__main__':
    main()

