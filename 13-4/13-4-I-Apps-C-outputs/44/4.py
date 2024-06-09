
def find_rectangle(n, m, x, y, a, b):
    # Initialize the rectangle as (0, 0, 0, 0)
    rect = (0, 0, 0, 0)
    
    # Iterate through all possible positions of the left-bottom point
    for i in range(x):
        for j in range(y):
            # Check if the current position is a valid position for the left-bottom point
            if i + a - 1 <= n and j + b - 1 <= m:
                # Calculate the right-up point of the current rectangle
                right = i + a - 1
                up = j + b - 1
                
                # Check if the current rectangle is valid
                if right <= n and up <= m:
                    # Calculate the area of the current rectangle
                    area = (right - i) * (up - j)
                    
                    # Check if the current rectangle is the largest one
                    if area > (rect[2] - rect[0]) * (rect[3] - rect[1]):
                        rect = (i, j, right, up)
    
    return rect

