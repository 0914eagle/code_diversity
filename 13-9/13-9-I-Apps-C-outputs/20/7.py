
def solve(n, points):
    # Calculate the area of the CBD polygon
    area = 0
    for i in range(n):
        area += points[i][0] * points[(i+1)%n][1] - points[i][1] * points[(i+1)%n][0]
    area = abs(area) / 2

    # Calculate the total length of the CBD polygon
    perimeter = 0
    for i in range(n):
        dx = points[(i+1)%n][0] - points[i][0]
        dy = points[(i+1)%n][1] - points[i][1]
        perimeter += (dx**2 + dy**2)**0.5

    # Calculate the expected distance traveled by the taxi
    expected_distance = perimeter * area / n

    return expected_distance

