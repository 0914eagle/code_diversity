
def f1(N, points, A):
    # Calculate the current area of the polygon
    current_area = f2(N, points)

    # Calculate the ratio of the new area to the current area
    ratio = A / current_area

    # Create a new list to store the resized polygon points
    resized_points = []

    # Loop through the original polygon points and resize them
    for point in points:
        x, y = point
        resized_points.append((x * ratio, y * ratio))

    return resized_points

def f2(N, points):
    # Calculate the area of the polygon
    area = 0
    for i in range(N):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % N]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(float, input().split())
        points.append((x, y))
    A = int(input())
    resized_points = f1(N, points, A)
    for x, y in resized_points:
        print(f"{x:.4f} {y:.4f}")

