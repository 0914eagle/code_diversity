
def get_max_score(n, T, a, t):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Loop through the problems
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Check if the current problem can be solved within the time limit
            if t[i - 1] <= T:
                # Calculate the maximum score for the current problem
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + a[i - 1])
            else:
                # If the current problem cannot be solved, copy the previous value
                dp[i][j] = dp[i - 1][j]
    
    # Return the maximum score and the number of problems solved
    return dp[n][n], n

def get_problems(n, a, t):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Loop through the problems
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Check if the current problem can be solved within the time limit
            if t[i - 1] <= T:
                # Calculate the maximum score for the current problem
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + a[i - 1])
            else:
                # If the current problem cannot be solved, copy the previous value
                dp[i][j] = dp[i - 1][j]
    
    # Initialize the list of problems to solve
    problems = []
    
    # Loop through the problems in reverse order
    for i in range(n, 0, -1):
        # Check if the current problem is part of the optimal solution
        if dp[i][n] > 0:
            # Add the current problem to the list of problems to solve
            problems.append(i)
    
    # Return the list of problems to solve
    return problems

if __name__ == '__main__':
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    score, k = get_max_score(n, T, a, t)
    problems = get_problems(n, a, t)
    print(score)
    print(k)
    print(*problems)

