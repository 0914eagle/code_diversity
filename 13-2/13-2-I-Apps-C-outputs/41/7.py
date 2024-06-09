
def count_intersections(lines):
    points = set()
    for line in lines:
        x0, y0, x1, y1 = line
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                points.add((x0, y))
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                points.add((x, y0))
        else:
            points.add((x0, y0))
            points.add((x1, y1))
    return len(points)

