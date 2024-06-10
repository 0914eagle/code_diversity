
def get_number_of_ways_to_paint_balls(n, k):
    # Initialize a 2D array to store the number of ways to paint each subarray
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    # Base case: only one way to paint an empty subarray
    for i in range(k+1):
        dp[0][i] = 1
    
    # Populate the 2D array using the recurrence relation
    for i in range(1, n+1):
        for j in range(1, k+1):
            for color in range(k):
                if color != j:
                    dp[i][j] += dp[i-1][color]
    
    # Return the number of ways to paint the entire array
    return dp[n][1]

def main():
    n, k = map(int, input().split())
    print(get_number_of_ways_to_paint_balls(n, k))

if __name__ == '__main__':
    main()

