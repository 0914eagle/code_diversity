
def get_key_points(n):
    key_points = []
    for i in range(n):
        x, y = map(int, input().split())
        key_points.append((x, y))
    return key_points

def get_levels(key_points):
    levels = {}
    for point in key_points:
        x, y = point
        level = max(x, y)
        if level not in levels:
            levels[level] = []
        levels[level].append(point)
    return levels

def get_min_distance(key_points, levels):
    distance = 0
    for level in sorted(levels.keys()):
        points = levels[level]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance += get_distance(points[i], points[j])
    return distance

def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    n = int(input())
    key_points = get_key_points(n)
    levels = get_levels(key_points)
    distance = get_min_distance(key_points, levels)
    print(distance)

if __name__ == '__main__':
    main()

