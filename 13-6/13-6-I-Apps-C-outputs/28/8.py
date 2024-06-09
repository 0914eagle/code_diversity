
def get_carpet_area(a, b, c):
    if a + b + c > 100:
        return -1
    
    # Calculate the area of the triangle
    area = (a * b * c) / 2
    
    return area

