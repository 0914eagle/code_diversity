
def get_paths(n, m, k, grid):
    # Initialize the dp table with all 0s
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # Base case: when we are at the last cell, the xor sum is just the number at that cell
    dp[n][m] = grid[n-1][m-1]
    
    # Loop through the grid in reverse order
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            # Get the xor sum of the current cell and the cell to the right and below it
            xor_sum = dp[i+1][j] ^ dp[i][j+1]
            
            # If the xor sum is equal to k, add the number at the current cell to the count
            if xor_sum == k:
                dp[i][j] += grid[i][j]
    
    return dp[0][0]

def main():
    n, m, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(get_paths(n, m, k, grid))

if __name__ == '__main__':
    main()

