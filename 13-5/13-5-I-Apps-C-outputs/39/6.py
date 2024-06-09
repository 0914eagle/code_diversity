
import sys

def f1(s):
    # Calculate the number of palindromic strings of length 2N that contain s as a subsequence
    n = len(s)
    mod = 1000000007
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][n]

def f2(s):
    # Calculate the number of palindromic strings of length 2N that contain s as a subsequence, but not necessarily contiguous
    n = len(s)
    mod = 1000000007
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][n]

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(s))
    print(f2(s))

