
def get_center_coordinates(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_mean = sum(x_coords) / len(x_coords)
    y_mean = sum(y_coords) / len(y_coords)
    return (x_mean, y_mean)

def get_height(points, center):
    heights = [point[2] for point in points]
    max_height = max(heights)
    return max_height

def main():
    points = []
    for _ in range(int(input())):
        x, y, h = map(int, input().split())
        points.append((x, y, h))
    center = get_center_coordinates(points)
    height = get_height(points, center)
    print(*center, height)

if __name__ == '__main__':
    main()

