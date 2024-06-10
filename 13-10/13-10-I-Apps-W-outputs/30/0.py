
def get_possible_photos(r, c, n, k):
    # Initialize a grid to represent the orchestra
    grid = [[0] * c for _ in range(r)]
    
    # Add violists to the grid
    for i in range(n):
        x, y = map(int, input().split())
        grid[x-1][y-1] = 1
    
    # Count the number of possible photos
    photos = 0
    for i in range(r):
        for j in range(c):
            # If the current cell is a violist, count the number of adjacent violists
            if grid[i][j] == 1:
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < r and 0 <= y < c and grid[x][y] == 1:
                            count += 1
                # If the number of adjacent violists is at least k, add 1 to the number of possible photos
                if count >= k:
                    photos += 1
    
    return photos

def main():
    r, c, n, k = map(int, input().split())
    print(get_possible_photos(r, c, n, k))

if __name__ == '__main__':
    main()

