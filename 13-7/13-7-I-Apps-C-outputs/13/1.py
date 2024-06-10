
def get_color_grid(r, c, i, j, n):
    # Initialize the grid with white color
    grid = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    grid[i-1][j-1] = 'A'
    
    # Set the direction of the zamboni
    direction = 'U'
    
    # Set the step size
    step_size = 1
    
    # Loop through the number of steps
    for _ in range(n):
        # Move the zamboni in the current direction
        if direction == 'U':
            i -= step_size
        elif direction == 'D':
            i += step_size
        elif direction == 'L':
            j -= step_size
        elif direction == 'R':
            j += step_size
        
        # Wrap the zamboni around the edges of the rink
        i = i % r
        j = j % c
        
        # Set the color of the current cell
        grid[i][j] = chr(ord('A') + (ord(grid[i][j]) - ord('A') + 1) % 26)
        
        # Rotate the direction of the zamboni
        direction = chr((ord(direction) + 1) % 4)
        
        # Increment the step size
        step_size += 1
    
    # Set the final location of the zamboni
    grid[i][j] = '@'
    
    return grid

def main():
    r, c, i, j, n = map(int, input().split())
    grid = get_color_grid(r, c, i, j, n)
    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    main()

