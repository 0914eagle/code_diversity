
def get_max_area(W, H, x, y):
    # Calculate the area of the two triangles formed by the line x=1 and the rectangle
    area1 = abs(x - 0) * min(y, H)
    area2 = abs(W - x) * min(y, H)
    area3 = abs(W - 0) * min(y - 0, H - y)
    area4 = abs(x - 0) * min(y - 0, H - y)
    
    # Calculate the maximum possible area
    max_area = max(area1, area2, area3, area4)
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    if max_area == area1 or max_area == area2:
        return max_area, 1
    else:
        return max_area, 0

