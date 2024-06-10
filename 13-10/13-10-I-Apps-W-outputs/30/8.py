
def count_pictures(r, c, n, k):
    # Initialize a grid to represent the orchestra
    grid = [[0] * c for _ in range(r)]
    
    # Place the violists in the grid
    for i in range(n):
        x, y = map(int, input().split())
        grid[x-1][y-1] = 1
    
    # Count the number of pictures Paul can take
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                count += 1
    
    return count

def main():
    r, c, n, k = map(int, input().split())
    print(count_pictures(r, c, n, k))

if __name__ == '__main__':
    main()

