
def solve(W, H, x, y):
    area_not_larger = 0
    multiple_ways = 0
    
    # Calculate the area of the rectangle
    rect_area = W * H
    
    # Calculate the area of the part not larger than the other
    for i in range(W+1):
        for j in range(H+1):
            if i * (H-j) <= rect_area - (W-i) * j:
                area_not_larger = max(area_not_larger, i * (H-j))
            else:
                area_not_larger = max(area_not_larger, (W-i) * j)
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    for i in range(W+1):
        for j in range(H+1):
            if i * (H-j) <= rect_area - (W-i) * j and area_not_larger == i * (H-j):
                multiple_ways = 1
                break
    
    return area_not_larger, multiple_ways

