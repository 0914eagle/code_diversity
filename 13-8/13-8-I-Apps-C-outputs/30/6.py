
def get_min_side_length(n, k, polygon):
    # Calculate the total area of the polygon
    total_area = 0
    for i in range(n):
        total_area += (polygon[i][0] * polygon[i-1][1]) - (polygon[i-1][0] * polygon[i][1])
    total_area = abs(total_area) / 2

    # Calculate the area of each map
    map_area = total_area / k

    # Calculate the side length of each map
    map_side_length = (map_area / n) ** 0.5

    return round(map_side_length, 2)

