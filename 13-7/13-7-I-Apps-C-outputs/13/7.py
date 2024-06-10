
import sys

def get_zamboni_location(r, c, i, j, n):
    # Initialize the zamboni location
    zamboni_location = [i, j]
    
    # Initialize the zamboni direction
    zamboni_direction = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    
    # Initialize the zamboni color
    zamboni_color = 'A'
    
    # Loop through the number of steps
    for step in range(n):
        # Move the zamboni in the current direction
        if zamboni_direction == 0: # up
            zamboni_location[0] -= 1
        elif zamboni_direction == 1: # right
            zamboni_location[1] += 1
        elif zamboni_direction == 2: # down
            zamboni_location[0] += 1
        else: # left
            zamboni_location[1] -= 1
        
        # Wrap the zamboni location if it goes off the edge of the rink
        if zamboni_location[0] < 1:
            zamboni_location[0] = r
        elif zamboni_location[0] > r:
            zamboni_location[0] = 1
        if zamboni_location[1] < 1:
            zamboni_location[1] = c
        elif zamboni_location[1] > c:
            zamboni_location[1] = 1
        
        # Rotate the zamboni direction 90 degrees clockwise
        zamboni_direction = (zamboni_direction + 1) % 4
        
        # Switch to the next color
        zamboni_color = chr(ord(zamboni_color) + 1)
        if zamboni_color == '[':
            zamboni_color = 'A'
    
    # Return the final zamboni location and color
    return [zamboni_location, zamboni_color]

def print_ice_rink(r, c, zamboni_location, zamboni_color):
    # Initialize the ice rink grid
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    
    # Fill in the ice rink grid with the zamboni location and color
    for i in range(r):
        for j in range(c):
            if [i+1, j+1] == zamboni_location:
                ice_rink[i][j] = '@'
            else:
                ice_rink[i][j] = zamboni_color
    
    # Print the ice rink grid
    for row in ice_rink:
        print(''.join(row))

if __name__ == '__main__':
    while True:
        # Read the input
        r, c, i, j, n = [int(x) for x in input().split()]
        
        # Check if the input is valid
        if r < 1 or r > 2000 or c < 1 or c > 2000 or i < 1 or i > r or j < 1 or j > c or n < 1 or n > 10**18:
            break
        
        # Get the final zamboni location and color
        zamboni_location, zamboni_color = get_zamboni_location(r, c, i, j, n)
        
        # Print the ice rink
        print_ice_rink(r, c, zamboni_location, zamboni_color)


