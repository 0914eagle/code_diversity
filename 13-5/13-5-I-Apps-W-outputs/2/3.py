
def get_tilings(w, h):
    # Initialize a 2D array to store the number of tilings for each sub-problem
    dp = [[0] * (h + 1) for _ in range(w + 1)]
    
    # Base case: only one way to tile a 1x1 square
    dp[1][1] = 1
    
    # Iterate over the width and height of the kitchen
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            # Iterate over the four possible orientations of the tile
            for k in range(4):
                # Get the coordinates of the top-left corner of the tile
                x = i - 1 + (k // 2) % 2
                y = j - 1 + (k % 2)
                
                # Check if the tile fits within the boundaries of the kitchen
                if x >= 0 and x < w and y >= 0 and y < h:
                    dp[i][j] += dp[x][y]
    
    # Return the number of tilings modulo 998244353
    return dp[w][h] % 998244353

def main():
    w, h = map(int, input().split())
    print(get_tilings(w, h))

if __name__ == '__main__':
    main()

