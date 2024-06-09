
def is_loop_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a list to store the segments
    segments = []

    # Loop through the points and create segments
    for i in range(len(sorted_points)):
        # Get the current point and the next point
        current_point = sorted_points[i]
        next_point = sorted_points[(i + 1) % len(sorted_points)]

        # Create a segment between the current point and the next point
        segment = [current_point, next_point]

        # Add the segment to the list of segments
        segments.append(segment)

    # Loop through the segments and check if they are perpendicular and do not intersect
    for i in range(len(segments)):
        # Get the current segment and the next segment
        current_segment = segments[i]
        next_segment = segments[(i + 1) % len(segments)]

        # Check if the current segment and the next segment are perpendicular
        if current_segment[0] == current_segment[1] or next_segment[0] == next_segment[1]:
            return False

        # Check if the current segment and the next segment intersect
        if current_segment[1] == next_segment[0] or current_segment[1] == next_segment[1]:
            return False

    # If all segments are perpendicular and do not intersect, return True
    return True

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Loop through the test cases
    for test_case in range(num_test_cases):
        # Read the number of points
        num_points = int(input())

        # Read the points
        points = []
        for i in range(num_points):
            x, y = map(int, input().split())
            points.append((x, y))

        # Check if it is possible to draw the loop
        if is_loop_possible(points):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

