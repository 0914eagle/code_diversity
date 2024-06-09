
def f1(S):
    # Calculate the number of palindromic strings of length 2N that contain S as a subsequence
    N = len(S)
    mod = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Initialize the dp table
    for i in range(N+1):
        dp[i][0] = 1
    
    # Fill in the dp table
    for i in range(1, N+1):
        for j in range(1, N+1):
            if S[i-1] == S[N-j]:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    
    # Return the result
    return dp[N][N]

def f2(S):
    # Calculate the number of palindromic strings of length 2N that contain S as a subsequence
    N = len(S)
    mod = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Initialize the dp table
    for i in range(N+1):
        dp[i][0] = 1
    
    # Fill in the dp table
    for i in range(1, N+1):
        for j in range(1, N+1):
            if S[i-1] == S[N-j]:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    
    # Return the result
    return dp[N][N]

if __name__ == '__main__':
    N = int(input())
    S = input()
    print(f1(S))
    print(f2(S))

