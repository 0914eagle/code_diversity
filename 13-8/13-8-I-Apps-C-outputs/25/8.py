
def get_longest_common_subsequence(strings):
    # Find the length of the longest common subsequence
    # of the first two strings
    lcs = len(get_lcs(strings[0], strings[1]))
    
    # Iterate over the rest of the strings
    for i in range(2, len(strings)):
        # Find the length of the longest common subsequence
        # of the current string and the previous strings
        lcs = max(lcs, len(get_lcs(strings[i], strings[i-1])))
    
    return lcs

def get_lcs(s1, s2):
    # Initialize the matrix to store the length of the LCS
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    # Fill in the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Find the length of the LCS
    lcs = 0
    for i in range(len(s1), 0, -1):
        for j in range(len(s2), 0, -1):
            if dp[i][j] > lcs:
                lcs = dp[i][j]
    
    return lcs

def main():
    n, k = map(int, input().split())
    strings = [input() for _ in range(n)]
    print(get_longest_common_subsequence(strings))

if __name__ == '__main__':
    main()

