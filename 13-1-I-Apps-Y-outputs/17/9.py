
def solve(a, b):
    # Initialize the minimum perimeter to infinity
    min_perimeter = float('inf')
    # Loop through all possible combinations of red and blue tiles
    for i in range(a + 1):
        for j in range(b + 1):
            # If the current combination forms a rectangle
            if i + j == a + b:
                # Calculate the perimeter of the rectangle
                perimeter = 2 * (i + j)
                # If the perimeter is less than the minimum perimeter, update the minimum perimeter
                if perimeter < min_perimeter:
                    min_perimeter = perimeter
    # Return the minimum perimeter
    return min_perimeter

