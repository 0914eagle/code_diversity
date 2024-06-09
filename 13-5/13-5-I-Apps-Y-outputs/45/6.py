
def get_max_area(W, H, x, y):
    # Calculate the area of the two parts
    area1 = abs(x * (H - y) - W * y)
    area2 = W * H - area1

    # Check if there are multiple ways to cut the rectangle
    if area1 == area2:
        return area1, 1
    else:
        return max(area1, area2), 0

