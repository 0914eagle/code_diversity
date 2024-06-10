
def get_longest_common_subsequence(strings):
    # Initialize a matrix to store the longest common subsequence
    dp = [[0] * (len(strings[0]) + 1) for _ in range(len(strings) + 1)]

    # Fill in the matrix
    for i in range(1, len(strings) + 1):
        for j in range(1, len(strings[0]) + 1):
            if strings[i - 1][j - 1] == strings[i - 2][j - 2]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the longest common subsequence
    return dp[-1][-1]

def main():
    n, k = map(int, input().split())
    strings = []
    for _ in range(n):
        strings.append(input())
    print(get_longest_common_subsequence(strings))

if __name__ == '__main__':
    main()

