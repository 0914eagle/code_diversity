
def get_optimal_platform_placement(points, k):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda x: x[0])

    # Initialize the optimal placement with the first platform placed at the leftmost point
    optimal_placement = [(sorted_points[0], sorted_points[0] + k)]

    # Iterate through the remaining points
    for i in range(1, len(sorted_points)):
        # Check if the current point is within the range of the current platform
        if sorted_points[i][0] <= optimal_placement[-1][1][0]:
            # If the current point is within the range, update the right border of the platform
            optimal_placement[-1][1] = (sorted_points[i] + k)
        else:
            # If the current point is not within the range, create a new platform
            optimal_placement.append((sorted_points[i], sorted_points[i] + k))

    return optimal_placement

def get_saved_points(platforms, points):
    # Initialize the saved points with an empty list
    saved_points = []

    # Iterate through the platforms
    for platform in platforms:
        # Iterate through the points
        for point in points:
            # Check if the point is within the range of the current platform
            if platform[0][0] <= point[0] <= platform[1][0]:
                # If the point is within the range, add it to the saved points
                saved_points.append(point)

    return saved_points

def main():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))

        platforms = get_optimal_platform_placement(points, k)
        saved_points = get_saved_points(platforms, points)

        print(len(saved_points))

if __name__ == '__main__':
    main()

