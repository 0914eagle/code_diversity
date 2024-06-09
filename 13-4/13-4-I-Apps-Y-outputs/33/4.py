
def f1(N, points, A):
    # Calculate the current area of the polygon
    current_area = calculate_area(points)

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = (A / current_area)**0.5

    # Resize the polygon
    resized_points = []
    for point in points:
        resized_points.append((point[0] * scaling_factor, point[1] * scaling_factor))

    return resized_points

def f2(N, points, A):
    # Calculate the current area of the polygon
    current_area = calculate_area(points)

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = (A / current_area)**0.5

    # Resize the polygon
    resized_points = []
    for point in points:
        resized_points.append((point[0] * scaling_factor, point[1] * scaling_factor))

    # Move the resized polygon to the north-east quadrant
    min_x = min(point[0] for point in resized_points)
    min_y = min(point[1] for point in resized_points)
    for i in range(len(resized_points)):
        resized_points[i] = (resized_points[i][0] - min_x, resized_points[i][1] - min_y)

    return resized_points

def calculate_area(points):
    area = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    return abs(area) / 2

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(float, input().split())
        points.append((x, y))
    A = int(input())
    resized_points = f2(N, points, A)
    for point in resized_points:
        print(f"{point[0]:.4f} {point[1]:.4f}")

