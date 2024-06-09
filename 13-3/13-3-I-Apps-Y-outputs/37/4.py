
def get_min_perimeter(a, b):
    # Initialize variables
    perimeter = 0
    red_tiles = 0
    blue_tiles = 0
    
    # Loop through all possible combinations of red and blue tiles
    for i in range(a + 1):
        for j in range(b + 1):
            # Check if the current combination forms a rectangle with the correct number of tiles
            if i + j == a + b:
                # Calculate the perimeter of the current rectangle
                perimeter = 2 * (i + j)
                
                # Check if the current rectangle has the minimum perimeter
                if perimeter < min_perimeter:
                    min_perimeter = perimeter
                    red_tiles = i
                    blue_tiles = j
    
    # Return the minimum perimeter and the number of red and blue tiles
    return min_perimeter, red_tiles, blue_tiles

