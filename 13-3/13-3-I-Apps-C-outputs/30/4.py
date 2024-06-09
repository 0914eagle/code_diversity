
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
        if do_intersect(smallest, largest, sorted_points[i], sorted_points[i + 1]):
            return False

    # Check if the line segment between the smallest and largest points intersects with the line segment between the points with the smallest and largest y-coordinates
    if do_intersect(smallest, largest, (smallest[0], smallest_y), (largest[0], largest_y)):
        return False

    return True

def do_intersect(p1, p2, q1, q2):
    # Check if the line segments p1-p2 and q1-q2 intersect
    if (q1[1] > p1[1] and q1[1] < p2[1]) or (q2[1] > p1[1] and q2[1] < p2[1]):
        return True
    if (p1[1] > q1[1] and p1[1] < q2[1]) or (p2[1] > q1[1] and p2[1] < q2[1]):
        return True
    return False

def count_in_danger_castles(nazis, castles):
    # Initialize the number of in-danger castles to 0
    in_danger_castles = 0

    # Iterate over each Nazi troop
    for nazi in nazis:
        # Find the four closest castles to the Nazi troop
        closest_castles = sorted(castles, key=lambda castle: distance(nazi, castle))[:4]

        # Check if the quadrilateral formed by the Nazi troop and the four closest castles is non-degenerate
        if is_non_degenerate_quadrilateral(closest_castles + [nazi]):
            in_danger_castles += 1

    return in_danger_castles

def distance(p1, p2):
    # Calculate the Euclidean distance between the two points
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

if __name__ == '__main__':
    # Read the number of Nazi troops and their positions
    num_nazis = int(input())
    nazis = []
    for _ in range(num_nazis):
        x, y = map(int, input().split())
        nazis.append((x, y))

    # Read the number of Soviet castles and their positions
    num_castles = int(input())
    castles = []
    for _ in range(num_castles):
        x, y = map(int, input().split())
        castles.append((x, y))

    # Count the number of in-danger castles
    in_danger_castles = count_in_danger_castles(nazis, castles)

    # Print the number of in-danger castles
    print(in_danger_castles)

