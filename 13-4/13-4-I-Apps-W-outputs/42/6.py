
def get_cost(c, a):
    if a == -1:
        return 0
    else:
        return c[a]

def solve(H, W, C, A):
    dp = [[0] * (W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + get_cost(C, A[i][j])
    return dp[H][W]

def main():
    H, W = map(int, input().split())
    C = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(H)]
    print(solve(H, W, C, A))

if __name__ == '__main__':
    main()

