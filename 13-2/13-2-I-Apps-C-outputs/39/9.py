
import math

def convex_hull(points):
    # Sort the points based on their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Create an empty list to store the convex hull
    hull = []

    # Iterate through the sorted points
    for p in sorted_points:
        # If the hull is empty, add the point to the hull
        if not hull:
            hull.append(p)
        # If the hull is not empty, check if the point is on the right side of the last line segment in the hull
        else:
            # Get the last two points in the hull
            last_point = hull[-1]
            prev_point = hull[-2]

            # Calculate the area of the triangle formed by the last two points in the hull and the current point
            area = (prev_point[0] * last_point[1] + last_point[0] * p[1] + p[0] * prev_point[1] - prev_point[0] * p[1] - last_point[0] * prev_point[1] - p[0] * last_point[1]) / 2

            # If the area is positive, the point is on the right side of the line segment, so add it to the hull
            if area > 0:
                hull.append(p)

    # Return the convex hull
    return hull

def get_score(points, hull):
    # Get the number of points inside the convex hull
    n = len(set(points) - set(hull))

    # Calculate the score
    score = 2 ** n

    # Return the score
    return score

def solve(points):
    # Get the convex hull of the points
    hull = convex_hull(points)

    # Get the score of the convex hull
    score = get_score(points, hull)

    # Return the score
    return score

def main():
    # Read the input points from stdin
    points = []
    for line in stdin:
        x, y = map(int, line.split())
        points.append((x, y))

    # Solve the problem
    score = solve(points)

    # Print the result
    print(score % 998244353)

if __name__ == "__main__":
    main()

