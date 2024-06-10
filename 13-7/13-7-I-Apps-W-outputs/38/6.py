
def get_valid_amidakuji_count(h, w, k):
    # Initialize a 2D array to store the valid amidakuji count
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    
    # Base case: when we are at the bottom of the last vertical line
    dp[h][0] = 1
    
    # Iterate through the vertical lines
    for i in range(h - 1, -1, -1):
        # Iterate through the horizontal lines
        for j in range(1, w + 1):
            # If we can reach the bottom of the current vertical line from the top of the previous vertical line
            if i + j <= h:
                # Add the number of valid amidakuji that can be formed by connecting the current horizontal line to the previous vertical line
                dp[i][j] += dp[i + j][j - 1]
    
    # Return the number of valid amidakuji that can be formed by connecting the first horizontal line to the first vertical line
    return dp[0][1]

def main():
    h, w, k = map(int, input().split())
    print(get_valid_amidakuji_count(h, w, k))

if __name__ == '__main__':
    main()

