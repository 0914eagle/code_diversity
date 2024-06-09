
def get_max_area(W, H, x, y):
    # Calculate the area of the rectangle
    area = W * H
    
    # Calculate the area of the two parts
    area1 = (W - x) * min(H, y)
    area2 = x * min(H, y)
    
    # Find the maximum area
    max_area = max(area1, area2)
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    if area1 == area2:
        return max_area, 1
    else:
        return max_area, 0

