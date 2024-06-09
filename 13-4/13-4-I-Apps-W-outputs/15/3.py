
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the minimum number of lines needed to cover all points as infinity
    min_lines = float('inf')

    # Iterate over all possible line combinations
    for i in range(len(sorted_points)):
        for j in range(i+1, len(sorted_points)):
            # Check if the line between the two points covers all points
            line_covers_all_points = True
            for point in sorted_points:
                if point not in line(sorted_points[i], sorted_points[j]):
                    line_covers_all_points = False
                    break

            # If the line covers all points, update the minimum number of lines needed
            if line_covers_all_points:
                min_lines = min(min_lines, 2)

    # Return whether it is possible to draw two lines to cover all points
    return min_lines == 2

def line(point1, point2):
    # Create a list of all points on the line between the two given points
    line_points = []
    for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            line_points.append((x, y))

    return line_points

n = int(input())
points = []

# Read the n points from stdin
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# Check if it is possible to draw two lines to cover all points
if is_possible(points):
    print("YES")
else:
    print("NO")

