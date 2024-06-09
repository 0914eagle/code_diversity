
def f1(n, points, area):
    # Calculate the current area of the polygon
    current_area = f2(n, points)

    # Calculate the scaling factor to achieve the desired area
    scaling_factor = (area / current_area) ** 0.5

    # Scale the polygon points
    scaled_points = [(x * scaling_factor, y * scaling_factor) for x, y in points]

    # Return the scaled points
    return scaled_points

def f2(n, points):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    area = abs(area) / 2

    # Return the area
    return area

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(float, input().split())
        points.append((x, y))
    area = int(input())
    scaled_points = f1(n, points, area)
    for x, y in scaled_points:
        print(f"{x:.4f} {y:.4f}")

