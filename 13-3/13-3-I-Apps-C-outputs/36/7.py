
def solve(nazis, castles):
    # Convert lists of x and y coordinates to pairs of x, y coordinates
    nazi_points = [(x, y) for x, y in zip(nazis[::2], nazis[1::2])]
    castle_points = [(x, y) for x, y in zip(castles[::2], castles[1::2])]

    # Find the convex hull of the Nazi points
    from scipy.spatial import ConvexHull
    hull = ConvexHull(nazi_points)

    # Count the number of castles that are in danger
    num_danger_castles = 0
    for castle in castle_points:
        if castle in hull.vertices:
            num_danger_castles += 1

    return num_danger_castles

