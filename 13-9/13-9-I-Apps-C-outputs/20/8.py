
def taxi_distance(n, points):
    # Calculate the area of the CBD polygon
    area = 0
    for i in range(n):
        area += points[i][0] * points[(i+1)%n][1] - points[i][1] * points[(i+1)%n][0]
    area = abs(area) / 2

    # Calculate the expected distance traveled by a taxi
    distance = 0
    for i in range(n):
        for j in range(i+1, n):
            point1 = points[i]
            point2 = points[j]
            segment_length = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
            segment_area = abs(point1[0] * point2[1] - point1[1] * point2[0])
            distance += segment_length * segment_area / area

    return distance

