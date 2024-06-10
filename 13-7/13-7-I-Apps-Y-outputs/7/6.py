
def get_min_distance(points):
    # Sort the points by their x-coordinate, then by their y-coordinate
    sorted_points = sorted(points, key=lambda point: (point[0], point[1]))

    # Initialize the minimum distance to 0
    min_distance = 0

    # Iterate through the points and calculate the distance between each pair of adjacent points
    for i in range(len(sorted_points) - 1):
        point1 = sorted_points[i]
        point2 = sorted_points[i + 1]
        distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        min_distance += distance

    return min_distance

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print(get_min_distance(points))

if __name__ == '__main__':
    main()

