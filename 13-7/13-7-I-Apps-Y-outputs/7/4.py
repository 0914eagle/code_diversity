
def get_min_distance(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Initialize the minimum distance to 0
    min_distance = 0

    # Iterate through the points and calculate the distance between them
    for i in range(len(sorted_points) - 1):
        min_distance += abs(sorted_points[i + 1][0] - sorted_points[i][0])

    return min_distance

def main():
    # Read the number of points from stdin
    n = int(input())

    # Read the points from stdin
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # Calculate the minimum distance
    min_distance = get_min_distance(points)

    # Print the minimum distance
    print(min_distance)

if __name__ == '__main__':
    main()

