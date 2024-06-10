
def get_subsequence_length(s, t):
    # Initialize variables
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Return the result
    return m - dp[n][m]

def main():
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    print(get_subsequence_length(s, t))

if __name__ == '__main__':
    main()

