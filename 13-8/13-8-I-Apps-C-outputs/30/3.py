
def solve(n, k, polygon):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += polygon[i][0] * polygon[i-1][1] - polygon[i-1][0] * polygon[i][1]
    area = abs(area) / 2

    # Calculate the side length of the square map
    side_length = (area / k) ** 0.5

    return round(side_length, 2)

