
def expected_distance(n, points):
    # Calculate the area of the CBD polygon
    area = 0
    for i in range(n):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    area = abs(area) / 2

    # Calculate the expected distance traveled by the taxi
    distance = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        distance += (x2-x1)**2 + (y2-y1)**2
    distance = (distance / n) ** 0.5

    # Return the expected distance traveled by the taxi
    return distance

