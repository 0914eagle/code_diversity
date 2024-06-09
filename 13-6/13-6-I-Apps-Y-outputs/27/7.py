
def is_achievable(M, N, C, A, X):
    # Initialize a 2D array to store the minimum amount of money needed to achieve the objective
    dp = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
    
    # Base case: when there are no books and no algorithms
    dp[0][0] = 0
    
    # Populate the 2D array with the minimum amount of money needed to achieve the objective
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + C[i-1])
    
    # Check if the objective is achievable
    if dp[N][M] <= X:
        return True
    else:
        return False

def get_minimum_amount(M, N, C, A, X):
    # Initialize a 2D array to store the minimum amount of money needed to achieve the objective
    dp = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
    
    # Base case: when there are no books and no algorithms
    dp[0][0] = 0
    
    # Populate the 2D array with the minimum amount of money needed to achieve the objective
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + C[i-1])
    
    # Return the minimum amount of money needed to achieve the objective
    return dp[N][M]

if __name__ == '__main__':
    M, N, C, A, X = map(int, input().split())
    C = [int(x) for x in input().split()]
    A = [list(map(int, input().split())) for _ in range(M)]
    print(get_minimum_amount(M, N, C, A, X))

