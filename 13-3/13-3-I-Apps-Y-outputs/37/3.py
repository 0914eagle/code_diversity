
def get_min_perimeter(a, b):
    # Initialize the minimum perimeter to infinity
    min_perimeter = float('inf')
    
    # Iterate over all possible positions of the rectangles
    for x in range(a + b):
        for y in range(a + b - x):
            # Check if the rectangle formed by the red tiles has the correct dimensions
            if x == a and y == b:
                # The perimeter of the rectangle is 2(a + b)
                min_perimeter = min(min_perimeter, 2 * (a + b))
            # Check if the rectangle formed by the blue tiles has the correct dimensions
            elif x == b and y == a:
                # The perimeter of the rectangle is 2(a + b)
                min_perimeter = min(min_perimeter, 2 * (a + b))
    
    # Return the minimum perimeter
    return min_perimeter

