
def max_manhattan_distance(points):
    max_dist = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            max_dist = max(max_dist, dist)
    return max_dist

