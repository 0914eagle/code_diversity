
import math

def get_distance(point1, point2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(point1, point2)))

def get_center(points):
    x_coords, y_coords, z_coords = zip(*points)
    x_center = sum(x_coords) / len(points)
    y_center = sum(y_coords) / len(points)
    z_center = sum(z_coords) / len(points)
    return x_center, y_center, z_center

def get_radius(center, points):
    return max(get_distance(center, point) for point in points)

def main():
    points = []
    for _ in range(4):
        x, y, z = map(float, input().split())
        points.append((x, y, z))
    center = get_center(points)
    radius = get_radius(center, points)
    print(center[0], center[1], center[2])

if __name__ == '__main__':
    main()

