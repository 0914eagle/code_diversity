
def get_cost(i, j, c):
    return c[i, j] if i != j else 0

def f1(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[get_cost(i, j, c) for j in range(W)] for i in range(H)]

    # Loop through each row
    for i in range(H):
        # Loop through each column
        for j in range(W):
            # If the current cell contains a digit, update the dp table with the minimum cost of turning the digit into 1
            if A[i, j] != -1:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + get_cost(A[i, j], A[i, j-1], c))
                dp[i][j] = min(dp[i][j], dp[i-1][j] + get_cost(A[i, j], A[i-1, j], c))
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + get_cost(A[i, j], A[i-1, j-1], c))

    # Return the minimum total cost to turn every digit on the wall into 1
    return min(dp[H-1][W-1], dp[H-1][W-2], dp[H-2][W-1])

def f2(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[get_cost(i, j, c) for j in range(W)] for i in range(H)]

    # Loop through each row
    for i in range(H):
        # Loop through each column
        for j in range(W):
            # If the current cell contains a digit, update the dp table with the minimum cost of turning the digit into 1
            if A[i, j] != -1:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + get_cost(A[i, j], A[i, j-1], c))
                dp[i][j] = min(dp[i][j], dp[i-1][j] + get_cost(A[i, j], A[i-1, j], c))
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + get_cost(A[i, j], A[i-1, j-1], c))

    # Return the minimum total cost to turn every digit on the wall into 1
    return min(dp[H-1][W-1], dp[H-1][W-2], dp[H-2][W-1])

if __name__ == '__main__':
    H, W = map(int, input().split())
    c = [[int(x) for x in input().split()] for _ in range(10)]
    A = [[int(x) for x in input().split()] for _ in range(H)]
    print(f1(H, W, c, A))
    print(f2(H, W, c, A))

