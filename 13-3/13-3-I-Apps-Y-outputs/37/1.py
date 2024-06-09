
def get_min_perimeter(a, b):
    # Initialize the minimum perimeter to infinity
    min_perimeter = float('inf')
    
    # Iterate over all possible positions of the rectangle
    for x in range(a + b):
        for y in range(a + b - x):
            # Check if the rectangle has the correct dimensions
            if x + y == a and x * y == b:
                # Calculate the perimeter of the rectangle
                perimeter = 2 * (x + y)
                
                # Update the minimum perimeter if necessary
                min_perimeter = min(min_perimeter, perimeter)
    
    # Return the minimum perimeter
    return min_perimeter

