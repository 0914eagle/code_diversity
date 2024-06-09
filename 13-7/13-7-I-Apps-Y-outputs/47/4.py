
def get_maximum_area(W, H, x, y):
    # Calculate the area of the two parts
    area_1 = abs(x * (H - y) - W * y)
    area_2 = (W - x) * H
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    if area_1 == area_2:
        return area_1, 1
    else:
        return max(area_1, area_2), 0

