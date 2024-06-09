
def get_stained_area(a, b, c):
    if a + b + c > 100:
        return -1
    
    # Calculate the area of the equilateral triangle
    area = (a * b * c) / (4 * (math.sqrt(3) / 2))
    
    return area

