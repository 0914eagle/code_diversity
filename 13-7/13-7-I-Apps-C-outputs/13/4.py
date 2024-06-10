
def get_ice_color(r, c, i, j, n):
    # Initialize the ice rink with white color
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the zamboni
    ice[i-1][j-1] = 'A'
    
    # Define the direction of the zamboni
    direction = 'UP'
    
    # Define the step size
    step_size = 1
    
    # Loop through the number of steps
    for _ in range(n):
        # Move the zamboni in the current direction
        if direction == 'UP':
            i -= step_size
        elif direction == 'DOWN':
            i += step_size
        elif direction == 'LEFT':
            j -= step_size
        elif direction == 'RIGHT':
            j += step_size
        
        # Wrap the zamboni around the edges of the rink
        i = i % r
        j = j % c
        
        # Change the color of the ice
        ice[i][j] = chr(ord(ice[i][j]) + 1)
        
        # Rotate the direction of the zamboni
        if direction == 'UP':
            direction = 'RIGHT'
        elif direction == 'RIGHT':
            direction = 'DOWN'
        elif direction == 'DOWN':
            direction = 'LEFT'
        elif direction == 'LEFT':
            direction = 'UP'
        
        # Increment the step size
        step_size += 1
    
    # Return the final state of the ice rink
    return ice

def main():
    r, c, i, j, n = map(int, input().split())
    ice = get_ice_color(r, c, i, j, n)
    for row in ice:
        print(''.join(row))

if __name__ == '__main__':
    main()

