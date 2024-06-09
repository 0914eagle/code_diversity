
def solve(nazis, castles):
    # Convert lists of x and y coordinates to pairs of x, y coordinates
    nazi_points = [(x, y) for x, y in zip(nazis[::2], nazis[1::2])]
    castle_points = [(x, y) for x, y in zip(castles[::2], castles[1::2])]

    # Find the convex hull of the Nazi points
    from scipy.spatial import ConvexHull
    hull = ConvexHull(nazi_points)

    # Find the castles that are inside or on the border of the convex hull
    in_danger_castles = []
    for castle in castle_points:
        if castle in hull.points or any(np.cross(np.subtract(castle, hull.points[i]), np.subtract(castle, hull.points[(i+1) % len(hull.points)])) == 0 for i in range(len(hull.points))):
            in_danger_castles.append(castle)

    return len(in_danger_castles)

