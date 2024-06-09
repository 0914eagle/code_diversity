
def get_min_key_presses(n, lines, r_1, c_1, r_2, c_2):
    # Initialize the minimum number of key presses to infinity
    min_presses = float('inf')
    
    # Loop through all possible directions (up, down, left, right)
    for direction in ['up', 'down', 'left', 'right']:
        # Get the new position of the cursor after pressing the current direction
        new_r, new_c = get_new_position(n, lines, r_1, c_1, direction)
        
        # If the new position is the same as the target position, we have found the minimum number of key presses
        if new_r == r_2 and new_c == c_2:
            min_presses = 1
            break
        
        # If the new position is not the same as the target position, recursively call the function to find the minimum number of key presses to reach the new position
        else:
            presses = 1 + get_min_key_presses(n, lines, new_r, new_c, r_2, c_2)
            if presses < min_presses:
                min_presses = presses
    
    return min_presses

def get_new_position(n, lines, r, c, direction):
    # Initialize the new position to the current position
    new_r, new_c = r, c
    
    # Update the new position based on the direction
    if direction == 'up':
        if r > 1:
            new_r -= 1
        if c > lines[r - 1]:
            new_c = lines[r - 1] + 1
    elif direction == 'down':
        if r < n:
            new_r += 1
        if c > lines[r]:
            new_c = lines[r] + 1
    elif direction == 'left':
        if c > 1:
            new_c -= 1
    elif direction == 'right':
        if c < lines[r] + 1:
            new_c += 1
    
    return new_r, new_c

n, lines = map(int, input().split())
lines = list(map(int, input().split()))
r_1, c_1, r_2, c_2 = map(int, input().split())

print(get_min_key_presses(n, lines, r_1, c_1, r_2, c_2))

