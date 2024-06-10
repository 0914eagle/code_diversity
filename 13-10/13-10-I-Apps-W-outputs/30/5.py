
def get_possible_photos(r, c, n, k):
    # Initialize a grid of violinists
    grid = [[0] * c for _ in range(r)]
    
    # Mark the positions of the violas
    for i in range(n):
        grid[x[i] - 1][y[i] - 1] = 1
    
    # Count the number of photos Paul can take
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                count += 1
                if count == k:
                    return count
    
    # If we reach this point, it means we didn't find k violas in a single row or column
    return 0

def main():
    r, c, n, k = map(int, input().split())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    print(get_possible_photos(r, c, n, k))

if __name__ == '__main__':
    main()

