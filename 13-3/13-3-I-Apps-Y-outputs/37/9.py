
def get_min_perimeter(a, b):
    # Initialize the minimum perimeter to infinity
    min_perimeter = float('inf')
    
    # Loop through all possible combinations of red and blue tiles
    for i in range(a):
        for j in range(b):
            # Calculate the perimeter of the current combination
            perimeter = 2 * (i + j)
            
            # Check if the perimeter is less than the minimum perimeter
            if perimeter < min_perimeter:
                # Update the minimum perimeter
                min_perimeter = perimeter
    
    # Return the minimum perimeter
    return min_perimeter

