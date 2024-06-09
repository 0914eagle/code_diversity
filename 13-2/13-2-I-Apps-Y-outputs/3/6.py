
def solve(coordinates):
    # Convert the coordinates to a list of tuples
    coordinates = [(x, y, h) for x, y, h in coordinates]
    
    # Initialize the center coordinates and height
    center_x, center_y = 0, 0
    height = 0
    
    # Iterate over the coordinates and calculate the center coordinates and height
    for x, y, h in coordinates:
        center_x += x
        center_y += y
        height = max(height, h)
    
    # Calculate the average center coordinates
    center_x //= len(coordinates)
    center_y //= len(coordinates)
    
    return center_x, center_y, height

