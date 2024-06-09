
def solve(a, b, w, x, c):
    # Initialize variables
    arthur_time = 0
    aleksander_time = 0
    arthur_ahead = False
    
    # Loop until Alexander gets ahead of Arthur
    while not arthur_ahead:
        # Arthur's operation
        if b >= x:
            b -= x
        else:
            a -= 1
            b = w - (x - b)
        
        # Aleksander's operation
        c -= 1
        
        # Check if Alexander is ahead of Arthur
        if c <= a:
            arthur_ahead = True
        
        # Increment times
        arthur_time += 1
        aleksander_time += 1
    
    # Return the minimum time needed for Alexander to get ahead of Arthur
    return aleksander_time

