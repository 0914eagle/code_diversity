
def find_minimum_side_length(n, k, vertices):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += vertices[i][0] * vertices[i-1][1] - vertices[i-1][0] * vertices[i][1]
    area = abs(area) / 2

    # Calculate the side length for each map
    side_length = (area / k) ** 0.5

    return round(side_length, 2)

