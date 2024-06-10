
def get_number_of_ways(n, k):
    # Initialize a 2D array to store the number of ways to paint the balls
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: only one ball can be painted with one color
    for i in range(k):
        dp[1][i] = 1
    
    # Iterate over the number of balls
    for i in range(2, n + 1):
        # Iterate over the number of colors
        for j in range(k):
            # Calculate the number of ways to paint the current ball with the current color
            dp[i][j] = sum(dp[i - 1][:j] + dp[i - 1][j + 1:])
    
    # Return the number of ways to paint all the balls
    return sum(dp[n])

def main():
    n, k = map(int, input().split())
    print(get_number_of_ways(n, k))

if __name__ == '__main__':
    main()

