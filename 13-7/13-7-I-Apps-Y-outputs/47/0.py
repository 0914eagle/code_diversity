
def solve(W, H, x, y):
    area_not_larger = 0
    multiple_ways = 0
    
    # Calculate the area of the rectangle
    rect_area = W * H
    
    # Calculate the area of the part to the left of the line x=x
    left_area = x * H
    
    # Calculate the area of the part to the right of the line x=x
    right_area = (W-x) * H
    
    # Calculate the area of the part above the line y=y
    top_area = W * y
    
    # Calculate the area of the part below the line y=y
    bottom_area = W * (H-y)
    
    # Calculate the maximum possible area of the part whose area is not larger than that of the other
    area_not_larger = max(left_area, right_area, top_area, bottom_area)
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    if area_not_larger == left_area or area_not_larger == right_area or area_not_larger == top_area or area_not_larger == bottom_area:
        multiple_ways = 1
    
    return area_not_larger, multiple_ways

