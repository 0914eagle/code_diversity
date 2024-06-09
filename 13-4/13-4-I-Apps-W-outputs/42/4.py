
def f1(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[c[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current cell is not -1, continue
            if A[i][j] == -1:
                continue

            # Loop through the neighbors of the current cell
            for k in range(max(0, i-1), min(H, i+2)):
                for l in range(max(0, j-1), min(W, j+2)):
                    # If the neighbor is not -1 and the current cell is not equal to the neighbor, update the dp table
                    if A[k][l] != -1 and A[i][j] != A[k][l]:
                        dp[i][j] = min(dp[i][j], dp[k][l] + c[A[i][j]])

    # Return the minimum total cost to turn all digits into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i][j] != -1)

def f2(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[c[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current cell is not -1, continue
            if A[i][j] == -1:
                continue

            # Loop through the neighbors of the current cell
            for k in range(max(0, i-1), min(H, i+2)):
                for l in range(max(0, j-1), min(W, j+2)):
                    # If the neighbor is not -1 and the current cell is not equal to the neighbor, update the dp table
                    if A[k][l] != -1 and A[i][j] != A[k][l]:
                        dp[i][j] = min(dp[i][j], dp[k][l] + c[A[i][j]])

    # Return the minimum total cost to turn all digits into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i][j] != -1)

if __name__ == '__main__':
    H, W = map(int, input().split())
    c = [int(x) for x in input().split()]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(f1(H, W, c, A))
    print(f2(H, W, c, A))

