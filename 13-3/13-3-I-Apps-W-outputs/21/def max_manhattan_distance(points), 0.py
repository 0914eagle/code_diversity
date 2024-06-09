
def max_manhattan_distance(points):
    max_dist = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = abs(x1-x2) + abs(y1-y2)
            if dist > max_dist:
                max_dist = dist
    return max_dist

