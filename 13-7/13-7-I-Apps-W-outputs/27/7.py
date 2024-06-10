
def solve(n, k, S, a):
    # Calculate the factorial of each number
    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i
    
    # Initialize the dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: no cubes chosen and no exclamation marks stuck
    dp[0][0] = 1
    
    # Iterate over the number of cubes chosen
    for i in range(1, n + 1):
        # Iterate over the number of exclamation marks stuck
        for j in range(1, k + 1):
            # Calculate the sum of the numbers on the chosen cubes
            sum_chosen = sum(a[i - 1:i + j])
            # If the sum is equal to S, add the number of ways to choose the current cube and stick an exclamation mark
            if sum_chosen == S:
                dp[i][j] += dp[i - 1][j - 1]
            # If the sum is less than S, add the number of ways to choose the current cube and stick an exclamation mark
            if sum_chosen < S:
                dp[i][j] += dp[i - 1][j]
            # If the sum is greater than S, add the number of ways to choose the current cube and not stick an exclamation mark
            if sum_chosen > S:
                dp[i][j] += dp[i - 1][j - 1]
    
    # Return the number of ways to choose the cubes and stick exclamation marks
    return dp[n][k]

def main():
    n, k, S = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, S, a))

if __name__ == '__main__':
    main()

