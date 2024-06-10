
def possible_photos(r, c, n, k):
    # Initialize a grid to represent the orchestra
    grid = [['*'] * c for _ in range(r)]
    
    # Loop through the positions of the violists and mark them in the grid
    for i in range(n):
        grid[violist_positions[i][0] - 1][violist_positions[i][1] - 1] = '#'
    
    # Initialize a counter for the number of possible photos
    count = 0
    
    # Loop through the grid and count the number of possible photos
    for i in range(r):
        for j in range(c):
            # If the current cell is a viola, count the number of adjacent violists
            if grid[i][j] == '#':
                count += 1
    
    # Return the number of possible photos
    return count

def main():
    # Read the input
    r, c, n, k = map(int, input().split())
    violist_positions = []
    for _ in range(n):
        violist_positions.append(list(map(int, input().split())))
    
    # Call the possible_photos function and print the result
    print(possible_photos(r, c, n, k))

if __name__ == '__main__':
    main()

