
def get_center_coordinates(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_mean = sum(x_coords) / len(x_coords)
    y_mean = sum(y_coords) / len(y_coords)
    return (x_mean, y_mean)

def get_height(points, center):
    heights = [point[2] for point in points]
    return max(heights) + abs(center[0]) + abs(center[1])

def main():
    num_points = int(input())
    points = []
    for _ in range(num_points):
        x, y, h = map(int, input().split())
        points.append((x, y, h))
    center = get_center_coordinates(points)
    height = get_height(points, center)
    print(center[0], center[1], height)

if __name__ == '__main__':
    main()

