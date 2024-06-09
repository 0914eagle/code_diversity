
def get_max_area(W, H, x, y):
    # Calculate the area of the two parts
    area_1 = abs(x * (H - y) - W * y)
    area_2 = W * H - area_1

    # Check if there are multiple ways to cut the rectangle
    if area_1 == area_2:
        return area_1, 1
    else:
        return area_1, 0

