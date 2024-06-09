
def max_manhattan_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            max_distance = max(max_distance, distance)
    return max_distance

