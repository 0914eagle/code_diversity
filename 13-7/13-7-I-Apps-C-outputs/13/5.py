
def get_ice_color(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white color
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    ice_rink[i-1][j-1] = '@'
    
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
        else:
            j += step_size
        
        # Wrap the zamboni around the edges of the rink
        i = i % r
        j = j % c
        
        # Set the color of the current cell
        ice_rink[i][j] = chr(ord('A') + (step_size - 1) % 26)
        
        # Rotate the direction of the zamboni
        direction = rotate_direction(direction)
        
        # Increment the step size
        step_size += 1
    
    return ''.join([''.join(row) for row in ice_rink])

def rotate_direction(direction):
    if direction == 'U':
        return 'R'
    elif direction == 'R':
        return 'D'
    elif direction == 'D':
        return 'L'
    else:
        return 'U'

if __name__ == '__main__':
    r, c, i, j, n = map(int, input().split())
    print(get_ice_color(r, c, i, j, n))

