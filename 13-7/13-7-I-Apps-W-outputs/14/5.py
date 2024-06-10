
def get_min_mp(H, W, C, A):
    # Initialize a 2D array to store the minimum MP required to turn a digit into 1
    dp = [[0] * (W + 1) for _ in range(H + 1)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current square does not contain a digit, skip it
            if A[i][j] == -1:
                continue

            # Initialize the minimum MP required to turn the current digit into 1 to infinity
            min_mp = float("inf")

            # Loop through all possible digits that can be turned into the current digit
            for k in range(10):
                # If the current digit is already 1, the minimum MP required is 0
                if k == 1:
                    mp = 0
                # If the current digit is not 1, find the minimum MP required to turn it into 1
                else:
                    mp = C[A[i][j]][k]

                # If the current square is not at the edge of the wall, consider the minimum MP required to turn the adjacent square into 1
                if i > 0 and A[i - 1][j] != -1:
                    mp += dp[i - 1][j]
                if j > 0 and A[i][j - 1] != -1:
                    mp += dp[i][j - 1]

                # Update the minimum MP required to turn the current digit into 1
                min_mp = min(min_mp, mp)

            # Store the minimum MP required to turn the current digit into 1
            dp[i][j] = min_mp

    # Return the minimum MP required to turn every digit on the wall into 1
    return dp[H - 1][W - 1]

def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(get_min_mp(H, W, C, A))

if __name__ == '__main__':
    main()

