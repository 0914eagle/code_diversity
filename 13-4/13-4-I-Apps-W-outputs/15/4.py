
def is_possible(n, points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables for the left and right endpoints of the lines
    left_x = sorted_points[0][0]
    right_x = sorted_points[-1][0]
    left_y = sorted_points[0][1]
    right_y = sorted_points[-1][1]

    # Iterate through the points and update the endpoints of the lines
    for i in range(1, n):
        current_x = sorted_points[i][0]
        current_y = sorted_points[i][1]

        # If the current point is to the right of the right endpoint, update the right endpoint
        if current_x > right_x:
            right_x = current_x
            right_y = current_y

        # If the current point is to the left of the left endpoint, update the left endpoint
        if current_x < left_x:
            left_x = current_x
            left_y = current_y

    # Check if the left and right endpoints are the same
    if left_x == right_x and left_y == right_y:
        return "YES"
    else:
        return "NO"

n = int(input())
points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print(is_possible(n, points))

