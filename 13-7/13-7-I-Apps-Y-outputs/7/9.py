
def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_level(point):
    return max(point[0], point[1])

def get_key_points_by_level(key_points):
    levels = {}
    for point in key_points:
        level = get_level(point)
        if level not in levels:
            levels[level] = [point]
        else:
            levels[level].append(point)
    return levels

def get_min_distance(key_points):
    levels = get_key_points_by_level(key_points)
    total_distance = 0
    for level in sorted(levels.keys()):
        points = levels[level]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                total_distance += get_distance(points[i], points[j])
    return total_distance

def main():
    n = int(input())
    key_points = []
    for i in range(n):
        x, y = map(int, input().split())
        key_points.append((x, y))
    print(get_min_distance(key_points))

if __name__ == '__main__':
    main()

