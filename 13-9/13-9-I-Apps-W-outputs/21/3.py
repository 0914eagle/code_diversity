
import math

def find_min_circle(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the minimum radius and center of the circle
    min_radius = 0
    center = (0, 0)

    # Loop through the points and update the minimum radius and center
    for i in range(len(points)):
        # Calculate the distance from the current point to the center of the circle
        dist = math.sqrt((points[i][0] - center[0]) ** 2 + (points[i][1] - center[1]) ** 2)

        # If the distance is greater than the current minimum radius, update the minimum radius and center
        if dist > min_radius:
            min_radius = dist
            center = points[i]

    return min_radius

# Main function
if __name__ == "__main__":
    # Read the input points from stdin
    points = []
    for line in sys.stdin:
        x, y = map(int, line.split())
        points.append((x, y))

    # Find the minimum radius of the circle
    min_radius = find_min_circle(points)

    # Print the minimum radius
    print(min_radius)

