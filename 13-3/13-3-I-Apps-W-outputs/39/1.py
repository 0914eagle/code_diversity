
def f1(N, M):
    # Initialize the dp array with 0s
    dp = [0] * (M + 1)
    
    # Base case: only one way to tile a table of size 1x1
    dp[1] = 1
    
    # Populate the dp array using the recurrence relation
    for i in range(2, M + 1):
        for j in range(1, N + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]
    
    # Return the result modulo 10^9
    return dp[M] % 1000000000

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    print(f1(N, M))

