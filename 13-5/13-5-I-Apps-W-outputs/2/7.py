
def get_tilings(w, h):
    # Initialize a 2D array to store the number of tilings for each possible rotation
    dp = [[0] * (h + 1) for _ in range(w + 1)]
    
    # Base case: no tiles
    for i in range(w + 1):
        dp[i][0] = 1
    
    # Base case: one tile
    for j in range(h + 1):
        dp[0][j] = 1
    
    # Fill in the 2D array using the recurrence relation
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 998244353
    
    return dp[w][h]

def main():
    w, h = map(int, input().split())
    print(get_tilings(w, h))

if __name__ == '__main__':
    main()

