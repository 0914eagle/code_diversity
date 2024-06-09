
def get_min_key_presses(n, a, r1, c1, r2, c2):
    # Initialize the minimum number of key presses to infinity
    min_presses = float('inf')
    
    # Loop through all possible positions of the cursor in the text editor
    for i in range(1, n+1):
        for j in range(1, a[i-1]+1):
            # If the current position is (r1, c1), update the minimum number of key presses
            if i == r1 and j == c1:
                min_presses = min(min_presses, get_key_presses(n, a, i, j, r2, c2))
    
    # Return the minimum number of key presses
    return min_presses

# Function to get the number of key presses to move the cursor from position (r, c) to position (r2, c2)
def get_key_presses(n, a, r, c, r2, c2):
    # Initialize the number of key presses to 0
    presses = 0
    
    # Loop until the cursor reaches the final position (r2, c2)
    while r != r2 or c != c2:
        # If the cursor is in the first line and needs to move up, do nothing
        if r == 1 and c == 1:
            pass
        # If the cursor is in the last line and needs to move down, move to the last position of the previous line
        elif r == n and c == a[n-1]+1:
            r -= 1
            c = a[n-2]+1
        # If the cursor needs to move up, move up to the previous line
        elif r > 1 and c == 1:
            r -= 1
        # If the cursor needs to move down, move down to the next line
        elif r < n and c == a[r-1]+1:
            r += 1
        # If the cursor needs to move left, move left to the previous position
        elif c > 1:
            c -= 1
        # If the cursor needs to move right, move right to the next position
        else:
            c += 1
        
        # Increment the number of key presses
        presses += 1
    
    # Return the number of key presses
    return presses

