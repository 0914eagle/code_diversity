
import numpy as np

def get_ice_grid(r, c, i, j, n):
    # Initialize the ice grid as a 2D array of white dots
    ice_grid = np.array([['.' for _ in range(c)] for _ in range(r)])
    
    # Set the starting location of the zamboni
    ice_grid[i-1, j-1] = '@'
    
    # Define the direction of movement and the current color
    direction = 'up'
    color = 'A'
    
    # Loop through each step
    for step in range(n):
        # Move the zamboni in the current direction
        if direction == 'up':
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        else:
            j += 1
        
        # Wrap the zamboni around the edge of the rink
        if i == 0:
            i = r
        if i == r+1:
            i = 1
        if j == 0:
            j = c
        if j == c+1:
            j = 1
        
        # Overwrite the current color on the ice
        ice_grid[i-1, j-1] = color
        
        # Switch to the next color in alphabetical order
        color = chr(ord(color) + 1)
        if color == 'Z':
            color = 'A'
        
        # Rotate the direction of the zamboni 90 degrees clockwise
        if direction == 'up':
            direction = 'right'
        elif direction == 'right':
            direction = 'down'
        elif direction == 'down':
            direction = 'left'
        else:
            direction = 'up'
    
    return ice_grid

def main():
    r, c, i, j, n = map(int, input().split())
    ice_grid = get_ice_grid(r, c, i, j, n)
    print(ice_grid)

if __name__ == '__main__':
    main()

