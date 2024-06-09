
def f1(N, M):
    # Initialize the dp array with 0s
    dp = [0] * (M + 1)
    
    # Base case: only one way to tile a table of size 1x1
    dp[1] = 1
    
    for i in range(2, M + 1):
        # Calculate the number of ways to tile a table of size 1xi
        dp[i] += dp[i - 1]
        
        # Calculate the number of ways to tile a table of size 2x(i - 1)
        if i - 1 >= 1:
            dp[i] += dp[i - 2]
    
    # Return the number of ways to tile the table of size NxM
    return dp[M]

def f2(N, M):
    # Initialize the dp array with 0s
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: only one way to tile a table of size 1x1
    dp[1][1] = 1
    
    for i in range(2, M + 1):
        # Calculate the number of ways to tile a table of size 1xi
        dp[1][i] += dp[1][i - 1]
        
        # Calculate the number of ways to tile a table of size 2x(i - 1)
        if i - 1 >= 1:
            dp[1][i] += dp[1][i - 2]
    
    for i in range(2, N + 1):
        # Calculate the number of ways to tile a table of size ix1
        dp[i][1] += dp[i - 1][1]
        
        # Calculate the number of ways to tile a table of size ix2
        if i - 1 >= 1:
            dp[i][1] += dp[i - 2][1]
    
    # Return the number of ways to tile the table of size NxM
    return dp[N][M]

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(f1(N, M))
    print(f2(N, M))

