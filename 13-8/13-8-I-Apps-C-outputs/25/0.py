
def get_lcs(strings):
    # Initialize a matrix to store the longest common subsequence
    dp = [[0] * (len(strings) + 1) for _ in range(len(strings[0]) + 1)]

    # Fill in the matrix
    for i in range(1, len(strings[0]) + 1):
        for j in range(1, len(strings) + 1):
            if strings[j - 1][i - 1] == strings[0][i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the longest common subsequence
    return dp[-1][-1]

def main():
    # Read the input
    n, k = map(int, input().split())
    strings = [input() for _ in range(n)]

    # Compute the longest common subsequence
    lcs = get_lcs(strings)

    # Print the result
    print(lcs)

if __name__ == '__main__':
    main()

