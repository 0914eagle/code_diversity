
def solve(W, H, x, y):
    # Calculate the area of the rectangle
    area = W * H
    
    # Calculate the area of the part to the left of the line x=x
    left_area = x * H
    
    # Calculate the area of the part to the right of the line x=x
    right_area = (W - x) * H
    
    # Calculate the maximum possible area of the part whose area is not larger than that of the other
    max_area = max(left_area, right_area)
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    if left_area == right_area:
        multiple_ways = 1
    else:
        multiple_ways = 0
    
    # Return the maximum area and whether there are multiple ways to cut the rectangle
    return max_area, multiple_ways

