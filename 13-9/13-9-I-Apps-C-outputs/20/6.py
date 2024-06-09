
def solve(n, points):
    # Calculate the area of the CBD polygon
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        area += x1*y2 - x2*y1
    area = abs(area) / 2

    # Calculate the length of each side of the CBD polygon
    lengths = []
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        length = ((x1-x2)**2 + (y1-y2)**2)**0.5
        lengths.append(length)

    # Calculate the expected distance traveled by a taxi
    expected_distance = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        length = ((x1-x2)**2 + (y1-y2)**2)**0.5
        expected_distance += length * area / (4 * length)

    return expected_distance

