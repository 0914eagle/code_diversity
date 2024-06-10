
def get_lcs(strings):
    # Initialization
    m = len(strings)
    n = len(strings[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill in the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if strings[i - 1][j - 1] == strings[0][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Return the length of the lcs
    return dp[m][n]

def main():
    n, k = map(int, input().split())
    strings = [input() for _ in range(n)]
    print(get_lcs(strings))

if __name__ == '__main__':
    main()

