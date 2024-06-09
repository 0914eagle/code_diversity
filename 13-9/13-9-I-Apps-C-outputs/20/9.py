
def get_expected_distance(n, points):
    # Calculate the area of the CBD polygon
    area = 0
    for i in range(n):
        area += points[i][0] * points[(i+1)%n][1] - points[i][1] * points[(i+1)%n][0]
    area = abs(area) / 2

    # Calculate the total distance traveled by the taxi
    total_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            total_distance += distance(points[i], points[j])

    # Calculate the expected distance
    expected_distance = total_distance / area
    return expected_distance

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

