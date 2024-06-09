
def get_maximum_area(w, h, x, y):
    # Calculate the area of the rectangle
    area = w * h
    
    # Calculate the area of the part to the left of the line x=x
    area_left = x * h
    
    # Calculate the area of the part to the right of the line x=x
    area_right = (w - x) * h
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    multiple_ways = False
    if x > 0 and x < w and y > 0 and y < h:
        multiple_ways = True
    
    # Return the maximum area and a boolean indicating if there are multiple ways to cut the rectangle and achieve that maximum
    return max(area_left, area_right), multiple_ways

