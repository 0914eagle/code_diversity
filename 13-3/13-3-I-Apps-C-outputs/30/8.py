
def is_non_degenerate_quadrilateral(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Find the two points with the smallest and largest x-coordinates
    smallest = sorted_points[0]
    largest = sorted_points[-1]

    # Find the point with the smallest y-coordinate among the points between the smallest and largest x-coordinates
    smallest_y = min(point[1] for point in sorted_points[1:-1])

    # Find the point with the largest y-coordinate among the points between the smallest and largest x-coordinates
    largest_y = max(point[1] for point in sorted_points[1:-1])

    # Check if the line segment between the smallest and largest points intersects with any of the other line segments
    for i in range(1, len(sorted_points) - 1):
        if do_intersect(sorted_points[i], sorted_points[i + 1], smallest, largest):
            return False

    # Check if the line segment between the smallest and largest points intersects with the line segment between the smallest y-coordinate point and the largest y-coordinate point
    if do_intersect(smallest, largest, smallest_y, largest_y):
        return False

    return True

def do_intersect(p1, p2, q1, q2):
    # Find the slopes of the line segments
    m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    m2 = (q2[1] - q1[1]) / (q2[0] - q1[0])

    # Check if the slopes are equal
    if m1 == m2:
        return False

    # Find the x-coordinate of the intersection point
    x = (q1[1] - p1[1] + m1 * p1[0] - m2 * q1[0]) / (m1 - m2)

    # Check if the intersection point is between the endpoints of the line segments
    if p1[0] <= x <= p2[0] and q1[0] <= x <= q2[0]:
        return True
    else:
        return False

def count_in_danger_castles(nazis, castles):
    in_danger_castles = 0
    for castle in castles:
        # Find the four closest Nazi troops to the castle
        closest_nazis = sorted(nazis, key=lambda nazi: distance(nazi, castle))[:4]

        # Check if the four closest Nazi troops form a non-degenerate quadrilateral
        if is_non_degenerate_quadrilateral(closest_nazis + [castle]):
            in_danger_castles += 1

    return in_danger_castles

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

if __name__ == '__main__':
    nazis = []
    castles = []

    # Read the number of Nazi troops and their positions
    num_nazis = int(input())
    for _ in range(num_nazis):
        x, y = map(int, input().split())
        nazis.append((x, y))

    # Read the number of castles and their positions
    num_castles = int(input())
    for _ in range(num_castles):
        x, y = map(int, input().split())
        castles.append((x, y))

    # Count the number of in-danger castles
    in_danger_castles = count_in_danger_castles(nazis, castles)

    # Print the number of in-danger castles
    print(in_danger_castles)

