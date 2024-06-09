
def is_possible_loop(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a list to store the segments
    segments = []

    # Iterate through the points and create segments
    for i in range(len(sorted_points)):
        # Get the current point and the next point
        current_point = sorted_points[i]
        next_point = sorted_points[(i + 1) % len(sorted_points)]

        # Create a segment between the current point and the next point
        segment = [current_point, next_point]

        # Add the segment to the list of segments
        segments.append(segment)

    # Check if the segments form a valid loop
    return is_valid_loop(segments)

def is_valid_loop(segments):
    # Check if the segments form a loop
    if len(segments) != len(set(segments)):
        return False

    # Check if the segments are perpendicular
    for i in range(len(segments)):
        current_segment = segments[i]
        next_segment = segments[(i + 1) % len(segments)]

        if current_segment[0] == next_segment[1] and current_segment[1] == next_segment[0]:
            return False

    # Check if the segments intersect
    for i in range(len(segments)):
        current_segment = segments[i]
        for j in range(i + 1, len(segments)):
            next_segment = segments[j]

            if current_segment[0] == next_segment[0] or current_segment[0] == next_segment[1] or current_segment[1] == next_segment[0] or current_segment[1] == next_segment[1]:
                return False

    return True

def main():
    # Read the input
    num_test_cases = int(input())
    for i in range(num_test_cases):
        num_points = int(input())
        points = []
        for j in range(num_points):
            x, y = map(int, input().split())
            points.append((x, y))

        # Check if it is possible to create a loop
        if is_possible_loop(points):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

