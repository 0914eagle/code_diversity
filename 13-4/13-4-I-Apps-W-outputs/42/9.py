
def get_min_mp(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[c[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current cell is not -1, we can skip it
            if A[i][j] == -1:
                continue

            # Loop through the neighbors of the current cell
            for k in range(max(0, i-1), min(H, i+2)):
                for l in range(max(0, j-1), min(W, j+2)):
                    # If the neighbor is not -1 and the cost of turning it into 1 is less than the current cost, update the cost
                    if A[k][l] != -1 and dp[k][l] + c[A[k][l]] < dp[i][j]:
                        dp[i][j] = dp[k][l] + c[A[k][l]]

    # Return the minimum total cost required to turn every digit on the wall into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i][j] != -1)

def main():
    H, W = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(get_min_mp(H, W, c, A))

if __name__ == '__main__':
    main()

