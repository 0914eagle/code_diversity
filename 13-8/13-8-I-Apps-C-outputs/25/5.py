
def get_input():
    n, k = map(int, input().split())
    strings = [input() for _ in range(n)]
    return n, k, strings

def longest_common_subsequence(strings):
    # Initialize a matrix to store the length of the longest common subsequence
    # for each pair of strings
    dp = [[0] * len(strings) for _ in range(len(strings))]

    # Fill in the matrix using the recursive formula
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + 1) if strings[i][-1] == strings[j][-1] else max(dp[i][j-1], dp[i-1][j])

    # Return the longest common subsequence length
    return max(max(row) for row in dp)

def main():
    n, k, strings = get_input()
    print(longest_common_subsequence(strings))

if __name__ == '__main__':
    main()

