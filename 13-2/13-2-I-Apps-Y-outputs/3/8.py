
def solve(coordinates):
    # Convert the coordinates to a list of tuples (x, y, h)
    coordinates = [(x, y, h) for x, y, h in coordinates]
    
    # Find the center coordinates (C_X, C_Y) by calculating the mean of the x and y coordinates
    C_X = sum([x for x, _, _ in coordinates]) / len(coordinates)
    C_Y = sum([y for _, y, _ in coordinates]) / len(coordinates)
    
    # Find the height H by calculating the maximum altitude of all the coordinates
    H = max([h for _, _, h in coordinates])
    
    return C_X, C_Y, H

