
def get_points(n):
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def get_sets(points, l, r, a):
    sets = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if points[i][0] < l or points[i][0] > r or points[j][0] < l or points[j][0] > r:
                continue
            if points[i][1] > a and points[j][1] > a:
                sets.append((points[i], points[j]))
    return sets

def count_sets(sets):
    count = 0
    for set in sets:
        if set not in count:
            count += 1
    return count

def main():
    n = int(input())
    points = get_points(n)
    l, r, a = map(int, input().split())
    sets = get_sets(points, l, r, a)
    print(count_sets(sets))

if __name__ == '__main__':
    main()

