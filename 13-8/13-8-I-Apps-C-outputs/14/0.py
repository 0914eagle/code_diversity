
def get_center(points):
    # Find the center of the sphere by taking the average of the coordinates of the points
    center = [0, 0, 0]
    for point in points:
        center[0] += point[0]
        center[1] += point[1]
        center[2] += point[2]
    center[0] /= len(points)
    center[1] /= len(points)
    center[2] /= len(points)
    return center

def get_radius(center, points):
    # Find the radius of the sphere by calculating the distance between the center and any of the points
    radius = 0
    for point in points:
        radius = max(radius, (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2 + (point[2] - center[2]) ** 2)
    return radius ** 0.5

def main():
    points = []
    for _ in range(4):
        points.append(list(map(float, input().split())))
    center = get_center(points)
    radius = get_radius(center, points)
    print(center[0], center[1], center[2])

if __name__ == '__main__':
    main()

