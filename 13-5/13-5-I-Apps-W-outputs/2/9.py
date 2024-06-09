
def get_tiling_count(w, h):
    # Initialize a 2D array to store the number of tilings for each cell
    dp = [[0] * (h + 1) for _ in range(w + 1)]
    
    # Base case: only one way to tile a 1x1 cell
    dp[1][1] = 1
    
    # Iterate over the width and height of the kitchen
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            # Iterate over the four possible orientations of the tile
            for k in range(4):
                # Get the coordinates of the neighboring cell
                x = i + (k // 2) - 1
                y = j + (k % 2) - 1
                
                # If the neighboring cell is within the bounds of the kitchen,
                # add the number of tilings for that cell to the current cell
                if 0 <= x <= w and 0 <= y <= h:
                    dp[i][j] += dp[x][y]
    
    # Return the number of tilings for the entire kitchen
    return dp[w][h]

def main():
    w, h = map(int, input().split())
    print(get_tiling_count(w, h) % 998244353)

if __name__ == '__main__':
    main()

